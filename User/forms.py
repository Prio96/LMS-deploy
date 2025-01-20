from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,UserModel,DepositModel
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email']
        
    def save(self):
        our_user=super().save()
        UserModel.objects.create(
            user=our_user
        )
        return our_user
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':(
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
            
class DepositForm(forms.ModelForm):
    class Meta:
        model=DepositModel
        fields=['amount']
        
    def __init__(self,*args,**kwargs):
        self.account=kwargs.pop('account')
        super().__init__(*args,**kwargs)
        
    def clean_amount(self):
        amount=self.cleaned_data.get('amount')
        
        if amount<0:
            raise forms.ValidationError(
                "Money can not be negative"
            )
        
        elif amount==0:
            raise forms.ValidationError(
                "Deposit some amount"
            )
        
        return amount
    def save(self,commit=True):
        self.instance.account=self.account
        return super().save()
        
        