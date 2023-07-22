from django.shortcuts import render, get_object_or_404
from blog.models import PostModel
from blog.forms import AddCommentForm

def detail(request, slug):
    post= get_object_or_404(PostModel, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        add_comment_form= AddCommentForm(data=request.POST)
        if add_comment_form.is_valid():
            comment= add_comment_form.save(commit=False) #hemen kaydetme
            comment.writer = request.user
            comment.post = post
            comment.save()
    else:
        add_comment_form= AddCommentForm()
    
    return render (request, 'pages/detail.html', context={
        'post':post,
        'comments':comments,
        'add_comment_form':add_comment_form
    })