from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel


#32 postModel icine models.Model yerine DateAbstractModel
class PostModel(DateAbstractModel):
    image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=50)
    content = RichTextField()
    #create_date = models.DateTimeField(auto_now=True)
    #update_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='post')  #birden fazla kategorisi olabilir
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'

    def __str__(self):
        return self.title