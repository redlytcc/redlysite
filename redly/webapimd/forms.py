from django import forms
from redweb.models import Chat

class FormChat(forms.ModelForm):
    def save(self,commit=True):
        chat=super(FormChat,self).save(commit=False)
        if commit:
            chat.save()
        return chat
    class Meta:
        model=Chat
        fields=['nome','text','img']
