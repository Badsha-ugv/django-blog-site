from django.urls import path
from . import views
urlpatterns = [
    path('',views.BlogList.as_view(),name = 'blog_list'),
    path('create_blog/',views.CreateBlog.as_view(), name='create_blog'),
    path('read_blog/<slug:slug>/',views.read_blog,name='read_blog'),
    

]