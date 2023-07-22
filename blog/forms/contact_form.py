from django import forms
from blog.models import ContactModel

#59. videoda bunlara gerek kalmadi
# class ContactForm(forms.Form):
#     email = forms.EmailField(max_length=100)
#     full_name = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
class ContactForm(forms.ModelForm):
    class Meta:
        model =ContactModel
        fields = {'email', 'full_name', 'message'}