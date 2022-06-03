# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'



class PostDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'