from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from .models import Blog,Comment,Likes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm


class BlogList(LoginRequiredMixin,ListView):
    context_object_name = 'blogs'
    model = Blog
    template = 'App_Blog/blog_list.html'

class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = "App_Blog/create_blog.html"
    fields = ('blog_title','blog_content','blog_image')
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-')+'-'+str(uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


@login_required
def read_blog(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('read_blog',kwargs={'slug':slug}))
    return render(request,'App_Blog/read_blog.html',context={'blog':blog,'comment_form':comment_form})

@login_required
def liked(request,pk):
    pass

