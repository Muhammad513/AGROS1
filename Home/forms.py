from django import forms
from django.forms import ModelForm
from .models import ChatMessage
class ChatMessageForm(ModelForm):
    class Meta:
        model=ChatMessage
        fields=['body',]




    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)
        self.fields['body'].widget.attrs.update({'class':"form-control","rows":1})    