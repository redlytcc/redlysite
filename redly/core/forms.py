from django import forms
from .models import User

class Logred(forms.Form):
    username=forms.CharField(label='Usuário',required=True,max_length=100,widget=forms.TextInput(attrs={'placeholder': ' '}))
    password=forms.CharField(label='Senha',widget=forms.PasswordInput(attrs={'placeholder': ' '}),required=True,max_length=100)

class CreateA(forms.ModelForm):
    password1=forms.CharField(label='Senha',required=True,widget=forms.PasswordInput(attrs={'placeholder': ' ','class':'Rpass'}))
    password2=forms.CharField(label='Novamente',required=True,widget=forms.PasswordInput(attrs={'placeholder': ' ','class':'Rpass R2'}))
    name=forms.CharField(label='Nome',max_length=40,required=True,widget=forms.TextInput(attrs={'placeholder': ' '}))
    username=forms.CharField(label='Apelido',max_length=40,required=True,widget=forms.TextInput(attrs={'placeholder': ' '}))
    email=forms.CharField(label='Email',max_length=60,required=True,widget=forms.EmailInput(attrs={'placeholder': ' '}))

    def clean_password2(self):
	    password1=self.cleaned_data.get("password1")
	    password2=self.cleaned_data.get("password2")
	    if password1 and password2 and password1!=password2:
	        raise forms.ValidationError('A confirmacao não está correta')
	    return password2

    def save(self, commit=True):
        user = super(CreateA, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            
            user.save()
        return user

    class Meta:
        model  = User
        fields = ['name','username','email']
