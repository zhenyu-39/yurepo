from django.shortcuts import render,redirect,reverse
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm,LoginForm
from django.contrib.auth import get_user_model,login,logout
import re

User = get_user_model()

# Create your views here.


@require_http_methods(['GET','POST'])
def yulogin(request):
    if request.method == 'GET':
        return render(request, 'html/login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            print(f"尝试登录: {email}")  # 调试信息
            print(f"用户存在: {user is not None}")
            if user and user.check_password(password):
                print("密码正确，正在登录...")
                #登录
                login(request, user)
                User.is_authenticated = True
                #判断用户是否需要记住我
                if not remember:
                    #如果没有点击记住我，那么就要设置过期时间为0，即浏览器关闭后就会过期
                    request.session.set_expiry(0)
                #如果点击了那就神那么都不做，使用默认的2周过期时间
                return redirect('/')
            else:
                # 账号不存在或密码错误
                return render(request, 'html/login.html', context={'error': '邮箱或密码错误，请重试。'})
        else:
            # 表单验证失败，展示第一条错误
            error_text = next(iter(form.errors.values()))[0] if form.errors else '表单验证失败'
            return render(request, 'html/login.html', context={'error': error_text})


def yulogout(request):
    logout(request)
    return redirect('/')


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'html/register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create_user(email=email, password=password, username=username)
            return redirect(reverse('yuauth:login'))
        else:
            print(form.errors)
            # 重新跳转到登录页面
            return redirect(reverse('yuauth:register'))
            # return render(request, 'html/register.html', {'form': form})


def is_valid_email(email):
    # 和前端保持完全一致的正则规则
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None

def send_email_captcha(request):
    # ?email=xxx
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code':400,'message':'必须传递邮箱！'})
    if not is_valid_email(email):
        return JsonResponse({'code':400,'message':'请输入有效的邮箱地址'})
    #生成验证码（取随机四位阿拉伯数字）
    #['0','2','2','1']
    captcha ="".join(random.sample(string.digits,4))
    #存储到数据库当中
    CaptchaModel.objects.update_or_create(email=email,defaults={'captcha':captcha})
    print(captcha)
    send_mail("yuzblog注册验证码",message=f'您的注册验证码是:{captcha}',recipient_list=[email],from_email=None)
    return JsonResponse({'code':200,'message':'邮箱发送成功'})
