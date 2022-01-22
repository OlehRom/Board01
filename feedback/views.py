from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def homepage(request):
    return render(request, 'advertisement/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Повідомлення"
            body = {
                'first_name': form.cleaned_data['Ім\'я'],
                'last_name': form.cleaned_data['Прізвище'],
                'email': form.cleaned_data['Пошта'],
                'message': form.cleaned_data['Повідомлення'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Заголовок некоректний')
            return redirect("feedback:homepage")

    form = ContactForm()
    return render(request, "feedback/contact.html", {'form': form})
