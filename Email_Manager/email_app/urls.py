from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inbox"),
    path("compose/", views.compose, name="compose"),
    path("sent/", views.sent, name="sent")
]