from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Email
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    user_email = request.user.email
    emails = Email.objects.filter(recipient=user_email)
    return render(request, "mail/inbox.html", {
        "emails": emails
    })

@login_required
def compose(request):
    # The form is populated with submitted data only after the user submits it (via a POST request). 
    # The first time the form is rendered (GET request), it's empty.
    print("Before form submission:", request.session)
    print(request.method)
    if request.method == 'POST':
        print("After form submission:", request.session)  # Log session after submitting
        # Get the form data
        sender = request.POST.get('sender')  
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # Save the email to the database
        Email.objects.create(sender=sender, recipient=recipient, subject=subject, body=body)
        
        return redirect('inbox')
        
    return render(request, "mail/compose.html", {
        'user_email': request.user.email  # Pass the logged-in user's email
    })

@login_required
def sent(request):
    user_email = request.user.email
    emails = Email.objects.filter(sender=user_email)
    return render(request, "mail/sent.html", {
        "emails": emails
    })



