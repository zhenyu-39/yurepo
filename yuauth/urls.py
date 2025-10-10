from django.urls import path
from . import views

app_name = 'yuauth'

urlpatterns=[
    path('login',views.yulogin,name='login'),
    path('register', views.register, name='register'),
    path('captcha',views.send_email_captcha,name='email_captcha'),
    path('logout',views.yulogout,name='logout'),
]