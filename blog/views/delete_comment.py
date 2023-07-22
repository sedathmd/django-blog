from django.contrib.auth.decorators import login_required
from blog.models import CommentModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required(login_url='/')
def delete_comment(request, id):
    comment = get_object_or_404(CommentModel, id=id)
    if comment.writer == request.user or comment.post.writer == request.user:
        comment.delete()
        #https://docs.djangoproject.com/en/4.2/ref/contrib/messages/
        messages.success(request, 'Comment successfully deleted')
        return redirect('detail', slug=comment.post.slug) #uygunsa buraya
    
    return redirect('main') #degilse buraya