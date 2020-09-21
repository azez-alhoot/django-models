from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DeleteView
from .models import Post

# class HomeView(TemplateView):
#     template_name = 'home.html'

class PostView(ListView):
    template_name = 'home.html'
    model = Post

class PostDetailsView(DeleteView):
    template_name = 'detail.html'
    model = Post
