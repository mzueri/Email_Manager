from django.db import models

class Email(models.Model):
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"From: {self.sender}, Subject: {self.subject}"
