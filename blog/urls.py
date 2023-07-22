from django.urls import path
from blog.views import contact, main, category, myposts, detail, add_post, update_post, delete_post, delete_comment
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', main, name='main'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myposts', myposts, name='myposts'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-post', add_post, name='add-post'),
    path('update-post/<slug:slug>', update_post, name='update-post'),
    path('delete-post/<slug:slug>', delete_post, name='delete-post'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),

    #views
    path('email-sent', TemplateView.as_view(template_name = 'pages/email-sent.html'), name='email-sent'),
    path('redirect', RedirectView.as_view(url='www.google.com'), name='redirect'), #herhangi bir yerde kullanmadim

]