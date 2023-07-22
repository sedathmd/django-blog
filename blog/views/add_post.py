from django.shortcuts import render, redirect
from blog.forms import AddPostForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add_post(request):
    form = AddPostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post =form.save(commit=False)  #hemen kaydetme
        post.writer = request.user  #writer'i current user'a esitle
        post.save() #simdi kaydet
        form.save_m2m() #bu category alani icin manytomany (birden cok)
        return redirect('detail', slug=post.slug) #olsurturdugu yazinin detayina gonder
    
    return render(request, 'pages/add-post.html', context={
        'form': form
    })