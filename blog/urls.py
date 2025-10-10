from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/detail/<int:blog_id>',views.blog_detail,name='blog_detail'),
    path('blog/pub',views.pub_blog,name='pub_blog'),
    path('blog/comment/pub',views.pub_comment,name='pub_comment'),
    path('search',views.search,name='search'),
    path('taking',views.taking_page,name='taking'),
    path('blog/taking',views.taking,name='blog_taking'),
    path('blog/delete/<int:blog_id>',views.delete,name='delete'),
    path('blog/delete/comment/<int:comment_id>',views.delete_comment,name='delete_comment'),
    path('blog/delete/image/<int:image_id>',views.delete_image,name='delete_image'),
    path('blog/house',views.house,name='house'),
]