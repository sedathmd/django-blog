from django.contrib.auth.decorators import login_required
from blog.models import PostModel
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='/')
def delete_post(request, slug):
    get_object_or_404(PostModel, slug=slug, writer=request.user).delete()
    return redirect('myposts')