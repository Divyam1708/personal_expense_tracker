from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from accounts.forms import UserCreateForm, UserLoginForm


def RegisterUser(request):
    if request.user.is_authenticated:
        return redirect('accounts:logged_in_user')
    
    else:
        if (request.method=='POST'):
            user_create_form=UserCreateForm(request.POST,prefix='user_create_form')
            if(user_create_form.is_valid()):
                create_user_object=user_create_form.save(commit=False)
                user_email=user_create_form.cleaned_data['email']
                user_password=user_create_form.cleaned_data['password']
                user_password2=user_create_form.cleaned_data['password2']
                if user_password==user_password2:
                    create_user_object.set_password(user_password)
                    create_user_object.save()
                    return redirect('accounts:login_user')
                    
                
        else:
            user_create_form=UserCreateForm(prefix='user_create_form')
            
        return render(
            request,
            'accounts/Register.html',
            context={
                'user_create_form':user_create_form,
            }
        )


def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('accounts:logged_in_user')
    
    else:
        if (request.method=='POST'):
            user_login_form=UserLoginForm(request.POST,prefix='user_login_form')
            if(user_login_form.is_valid()):
                email=user_login_form.cleaned_data['email']
                password=user_login_form.cleaned_data['password']
                user=authenticate(request,username=email,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('expenses:home')
                else:
                    print(user_login_form.errors)
        
        else:
            user_login_form=UserLoginForm(prefix='user_login_form')
        
        return render(
            request,
            'accounts/Login.html',
            context={
                'user_login_form':user_login_form,
            }
        )




def LoggedIn(request):
    
    return render(
        request,
        'accounts/Logged_in.html',
        context={
            'user':request.user,
        }
    )





def LogoutUser(request):
    logout(request)
    return redirect('accounts:login_user')

def csrf_error_page(request,reason=''):
    return render(
        request,
        'base/csrf_template.html',
        context={
            'reason':reason,
        },
        status=403
    )