from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel

class EditProfileForm(UserChangeForm):
    password = None  #sifreyi degistirme
    class Meta:
        model = CustomUserModel
        fields = ('email', 'first_name', 'last_name', 'avatar')