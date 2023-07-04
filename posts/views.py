from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    comment_form = CommentForm()

    context = {
        'posts':posts,
        'comment_form': comment_form,
    }

    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts:index')


def comments_create(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('posts:index')
