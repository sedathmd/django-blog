from django.contrib.auth import logout
from django.shortcuts import redirect

def log_out(request):
    #alttaki logout yukaridaki kütüphaneden gelir. 
    #icinde bulundugu method adi ile ilgili degil
    logout(request)
    return redirect('main')