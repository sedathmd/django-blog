from django.db import models
#from django.contrib.auth.models import User
from blog.models import PostModel
from blog.abstract_models import DateAbstractModel

#32 commentModel icine models.Model yerine DateAbstractModel
class CommentModel(DateAbstractModel):
    #releated_name'ler iliskilendirmek icin
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment') 
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    #create_date = models.DateTimeField(auto_now=True)
    #update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.writer.username