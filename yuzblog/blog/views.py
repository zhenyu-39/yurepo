from django.shortcuts import render,redirect,reverse
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from .models import BlogCategory,Blog,BlogComment,BlogImage
from .forms import PubBlogForm
from django.db.models import Q


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request,'html/index.html',context={'blogs':blogs})

def blog_detail(request,blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None
    return render(request,'html/blog_detail.html',context={'blog':blog})


# @login_required(login_url=reverse_lazy('yuauth:login'))
@require_http_methods(['GET','POST'])
@login_required()
def pub_blog(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request,'html/pub_bolg.html',context={'categories':categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title,content=content,category_id=category_id,author=request.user)
            return JsonResponse({'code':200,'message':'博客发布成功','data':{'blog_id':blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code':400,'message':'参数错误'})

@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(blog_id=blog_id,content=content,author=request.user)
    #重新加载博客详情页
    return redirect(reverse('blog:blog_detail',kwargs={'blog_id':blog_id}))

@require_GET
def search(request):
    #/search?q=xxx
    q = request.GET.get('q','').strip()
    #从博客的标题和内容中查找含有关键字的博客
    blogs = Blog.objects.filter(Q(title__icontains=q)|Q(content__icontains=q)).all()
    return render(request,'html/index.html',context={'blogs':blogs})

@require_POST
@login_required()
def taking(request):
    content = request.POST.get('content', '').strip()
    if not content:
        return JsonResponse({'code':400,'message':'内容不能为空'}, status=400)
    BlogImage.objects.create(content=content,author=request.user)
    return JsonResponse({'code':200,'message':'留言成功'})

@require_GET
def taking_page(request):
    images = BlogImage.objects.all()
    return render(request,'html/taking.html', context={'images': images})