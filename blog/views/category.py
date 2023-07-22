from django.shortcuts import render, get_object_or_404
from blog.models import CategoryModel
from django.core.paginator import Paginator

def category(request, categorySlug):
    category= get_object_or_404(CategoryModel, slug = categorySlug)
    posts= category.post.order_by('-id')  #buradaki post models/post.py deki category'nin releated name'inden geliyor
    
    page = request.GET.get('p')
    paginator = Paginator(posts,2)
    return render(request, 'pages/category.html', context={
        'posts' : paginator.get_page(page),
        'category_name' : category.name  #category.htmlde title'a vermek icin
    })