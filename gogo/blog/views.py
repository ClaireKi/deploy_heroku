from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Post
import datetime
from .form import PostForm
# Create your views here.

def index(request):
    user = request.user
    if user.is_active:
        posts = Post.objects.all().order_by('-id')
        return render(request, 'index.html', {'posts_show':posts})
    else:
        return render(request, 'plzLogin.html')

def new(request):
    return render(request, 'old_new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/blog/'+str(post.id))

def detail(request, post_id):
    user = request.user
    if user.is_active:
        post_detail = get_object_or_404(Post, pk = post_id)
        return render(request, 'detail.html', {'post':post_detail})
    else:
        return render(request, 'plzLogin.html')

def modify(request, post_id):
    user = request.user
    if user.is_active:
        post_detail = get_object_or_404(Post, pk = post_id)
        return render(request, 'modify.html', {'post':post_detail})
    else:
        return render(request, 'plzLogin.html')

def update(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.save()
    return redirect('/blog/'+str(post.id))

def delete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('index')

def newpost(request):
    user = request.user
    if user.is_active:
        if request.method == 'POST':
            form = PostForm(request.POST) # form을 불러오는 코드이다.
            if form.is_valid(): # 이 form 이 유효한지 확인해 주는 코드이다.
                post = form.save(commit = False) # 저장하지 않고 객체를 가져온다.
                post.pub_date = timezone.now()
                post.save()
                return redirect('index')
        else:
            form = PostForm()
            return render(request, 'new.html', {'form':form})
    else:
        return render(request, 'plzLogin.html')


