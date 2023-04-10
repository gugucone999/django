from django.http import JsonResponse
from django.shortcuts import render, redirect
from board.forms import BoardForm
from board.models import Board
from django.db.models import Q
from django.contrib.auth.decorators import login_required




@login_required(login_url='/user/login')
def update(request, bid):
    post = Board.objects.get(Q(id=bid))
    if request.user != post.writer:
        return redirect('/')
    if request.method == "GET":
        # boardForm = BoardForm(instance=post)
        return render(request, 'board/update.html', {'post':post})
    elif request.method == "POST":
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            post.title = boardForm.cleaned_data['title']
            post.contents = boardForm.cleaned_data['contents']
            post.save()
            return redirect('/')

@login_required(login_url='/user/login')
def register(request):
    if request.method == "GET":
        boardForm = BoardForm()
        return render(request, 'board/register.html', {'boardForm': boardForm})
    elif request.method == "POST":
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.writer = request.user
            board.save()
            return redirect('/')

@login_required(login_url='/user/login')
def delete(request, bid):
    post = Board.objects.get(Q(id=bid))
    if request.user != post.writer:
        return redirect('/')
    post.delete()
    return redirect('/')

def read(request, bid):
    post = Board.objects.get(Q(id=bid))
    return render(request, 'board/read.html',{'post': post})

def list(request):
    posts = Board.objects.all().order_by('-id')
    return render(request, 'board/list.html', {'posts': posts})
def rest_list(request):
    posts = Board.objects.all().order_by('-id')
    json = {'posts':[]}
    for post in posts:
        json['posts'].append({"title":post.title,
                              "contents":post.contents})
    return JsonResponse(json)

@login_required(login_url='/user/login')
def like(request, bid):
    post = Board.objects.get(Q(id=bid))
    user = request.user
    if post.like.filter(id=user.id).exists():
        post.like.remove(user)
        message = "del like"
    else :
        post.like.add(user)
        message = "add like"
    return JsonResponse({'message':message,
                         'like_cnt':post.like.count()})
