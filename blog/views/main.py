from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator
from django.db.models import Q


def main(request):  
    posts= PostModel.objects.order_by('-id')
    #52
    query =request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct() 
    #52 end
    #48
    page = request.GET.get('p')
    paginator = Paginator(posts,2)
    #48 end
    
    return render(request, 'pages/main.html', context={
        'posts' : paginator.get_page(page)
    })