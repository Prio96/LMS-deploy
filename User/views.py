from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,ListView,CreateView
from django.views import View
from .forms import UserRegistrationForm,DepositForm
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from Borrow.models import BorrowModel
from .models import DepositModel
from datetime import *
# Create your views here.
class UserRegistrationView(FormView):
    template_name='register.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('Register')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user=form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('Home')
    
@login_required
def UserLogoutView(request):
    logout(request)
    return redirect("Home")

class ProfileView(LoginRequiredMixin,ListView):
    template_name="profile.html"
    model=BorrowModel
    context_object_name="borrow_list"
    
    def get_queryset(self):
        queryset=super().get_queryset().filter(
            account=self.request.user.modifieduser
        )
        
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date=datetime.strptime(end_date_str,"%Y-%m-%d").date()
            queryset=queryset.filter(borrow_date__date__gte=start_date,borrow_date__date__lte=end_date)#for filtering through account
            
        return queryset.distinct()#distinct deyao jabe nao deya jabe
    
    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context.update({
    #         'reader':self.request.user.account
    #     })
    #     return context

class DepositView(LoginRequiredMixin,CreateView):
    template_name='deposit_form.html'
    form_class=DepositForm
    model=DepositModel
    success_url=reverse_lazy("Home")
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update(
            {
                'account':self.request.user.modifieduser
            }
        )
        return kwargs
    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.modifieduser
        account.balance+=amount
        account.save(
            update_fields=['balance']
        )
        form.save()
        message=render_to_string("deposit_email.html",{
            'user':self.request.user,
            'amount':amount,
        })
        send_email=EmailMultiAlternatives("Deposit Money", '', to=[self.request.user.email])
        send_email.attach_alternative(message,"text/html")
        send_email.send()
        messages.success(self.request,f"Successfully deposited ${amount}")
        return super().form_valid(form)
    


