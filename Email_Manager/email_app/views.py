from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, "hello/index.html")

def index(request):
    return render(request, "mail/inbox.html")

def compose(request):
    return render(request, "mail/compose.html")

def sent(request):
    return render(request, "mail/sent.html")



