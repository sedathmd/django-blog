from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myposts(request):
    posts = request.user.posts.order_by('-id') #buradaki posts models/post.py deki writer'ın releated name'inden geliyor
    page = request.GET.get('p')
    paginator = Paginator(posts, 2)

    return render(request, 'pages/myposts.html', context={
        'posts': paginator.get_page(page),
    })