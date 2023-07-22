from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import UpdatePostForm
from django.contrib.auth.decorators import login_required
from blog.models.post import PostModel

@login_required(login_url='/')
def update_post(request, slug):
    post = get_object_or_404(PostModel, slug=slug, writer=request.user)
    form = UpdatePostForm(request.POST or None, files=request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('detail', slug=post.slug)
    return render(request, 'pages/update-post.html', context={
        'form': form
    })