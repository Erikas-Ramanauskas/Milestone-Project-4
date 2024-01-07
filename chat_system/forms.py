from django import forms
from .models import MessageContent


class MessageContentForm(forms.ModelForm):
    class Meta:
        model = MessageContent
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Send message...'})
        }
