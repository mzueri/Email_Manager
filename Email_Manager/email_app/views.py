from django.shortcuts import render
from django.http import HttpResponse
from .models import Email

# Create your views here.
def index(request):
    return render(request, "mail/inbox.html", {
        "emails": Email.objects.all()
    })

def compose(request):
    return render(request, "mail/compose.html")

def sent(request):
    return render(request, "mail/sent.html", {
        "emails": Email.objects.all()
    })



