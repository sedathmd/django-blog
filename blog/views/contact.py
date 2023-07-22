from django.shortcuts import redirect, render
from blog.forms import ContactForm
from blog.models import ContactModel

#burada templates/pages... diye yazmamiza gerek yok 
#cünkü render zaten sadece templates klasorlerinin icine bakar
def contact(request):
    form = ContactForm()
    if request.method== 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # communication =ContactModel()
            # communication.email = form.cleaned_data['email']
            # communication.full_name = form.cleaned_data['full_name']
            # communication.message = form.cleaned_data['message']
            # communication.save()
            form.save()
            return redirect('email-sent')
    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context=context)
    #context vermeyeceksek {} veririz