from django.urls import path
from account.views import log_out, change_password, edit_profile, register
from django.contrib.auth import views as auth_views  #login icin

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
    ), name='login'),
    path('logout', log_out, name='logout'),
    path('change-password', change_password, name='change-password'),
    path('edit-profile', edit_profile, name='edit-profile'),
    path('register', register, name='register'),
]