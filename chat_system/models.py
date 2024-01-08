from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class MessageContent(models.Model):
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Messages(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    messages = models.ManyToManyField(
        MessageContent, blank=True, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    last_message = models.CharField(
        max_length=200, null=True, blank=True)
    last_message_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f"Sender: {self.sender} - Product: {self.product}"
