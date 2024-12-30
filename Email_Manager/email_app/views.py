from django.shortcuts import render
from django.http import HttpResponse
from .models import Email


# Create your views here.
def index(request):
    return render(request, "mail/inbox.html", {
        "emails": Email.objects.all()
    })


def compose(request):
    # The form is populated with submitted data only after the user submits it (via a POST request). 
    # The first time the form is rendered (GET request), it's empty.
    print(request.method)
    if request.method == 'POST':
        # Get the form data
        sender = request.POST.get('sender')  
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Save the email to the database
        Email.objects.create(sender=sender, recipient=recipient, subject=subject, body=body)
        
        return render(request, "mail/inbox.html", {"emails": Email.objects.all()})
        
    return render(request, "mail/compose.html")


def sent(request):
    return render(request, "mail/sent.html", {
        "emails": Email.objects.all()
    })



