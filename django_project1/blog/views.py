from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post 
from .forms import PostForm
#from django.http import HttpResponse


def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'This post has been created successfully')
            return redirect('posts')
        else: 
            messages.error(request, 'Please correct the following orders')
            return render(request, 'blog/post_form.html', {'form':form})

def home(request):
    posts = Post.objects.all()
    context ={'posts':posts}
    return render(request,'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>About</h1>')
    return render(request,'blog/about.html')