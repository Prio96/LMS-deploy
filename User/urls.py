from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserLogoutView,ProfileView,DepositView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='Register'),
    path('login/',UserLoginView.as_view(),name='Login'),
    path('logout/',UserLogoutView,name='Logout'),
    path('profile/',ProfileView.as_view(),name='Profile'),
    path('deposit/',DepositView.as_view(),name='Deposit'),
]