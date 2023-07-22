from django import forms
from blog.models import PostModel


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ('writer', 'slug') #writer ve slug haric