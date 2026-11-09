



from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not all((name, email, subject, message)):
            messages.error(request, 'Please complete every field before sending your message.')
        else:
            send_mail(
                subject=f'Website contact: {subject}',
                message=f'From: {name} <{email}>\n\n{message}',
                from_email=email,
                recipient_list=[ 'webmaster@localhost' ],
                fail_silently=False,
            )
            messages.success(request, 'Thank you. Your message has been sent.')

    return render(request, 'contact.html')

def page_not_found(request):
    return render(request, '404.html', status=404)
