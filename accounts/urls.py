from django.urls import path, include
from accounts import views

app_name='accounts'

urlpatterns = [
    path('',views.RegisterUser,name='regsiter_user'),
    path('login',views.LoginUser,name='login_user'),
    path('loggedin',views.LoggedIn,name='logged_in_user'),
    path('edit-user-information',views.EditUserInformation, name='edit-user-information'),
    path('logout',views.LogoutUser,name='logout_user')
]
