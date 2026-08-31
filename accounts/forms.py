from accounts import models
from django import forms

class UserCreateForm(forms.ModelForm):
    
    password=forms.CharField(max_length=40,min_length=4,widget=forms.PasswordInput(
    ),label='Enter Password')
    
    password2=forms.CharField(max_length=40,min_length=4,widget=forms.PasswordInput(
    ),label='Re-Enter Password')
    
    class Meta:
        model=models.User
        fields=['email','password','password2']
        
    def clean(self):
        cd=super().clean()
        pword=cd.get('password')
        pword2=cd.get('password2')
        
        if pword!=pword2:
            raise forms.ValidationError('PASSWORD NOT MATCHED.')
    
        return cd        



class UserLoginForm(forms.Form):
    email=forms.EmailField(
        widget=forms.EmailInput(
            
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            
        )
    )



class UserInfoEditForm(forms.ModelForm):
    class Meta:
        model=models.User
        exclude=['password','email','active','groups','last_login','is_superuser','is_active','is_staff','user_permissions','date_joined']
    