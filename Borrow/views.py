from django.shortcuts import render,redirect
from .models import BorrowModel,BookModel,UserModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,ListView,CreateView
from django.views import View
from django.contrib import messages
# from .forms import UserRegistrationForm,DepositForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from datetime import *
# Create your views here.
@login_required
def BorrowBookView(request,id):
    book=BookModel.objects.get(pk=id)
    account=request.user.modifieduser
    if account.balance>=book.borrowing_price:
        messages.success(request,f"You have successfully borrowed the book for ${book.borrowing_price}")
        account.balance-=book.borrowing_price
        account.save(update_fields=['balance'])
        borrow_obj=BorrowModel.objects.create(
            account=account,
            book=book,
            balance_after_borrowing=account.balance
        )
        borrow_obj.save()
        message=render_to_string("borrow_email.html",{
            'user':request.user,
            'amount':book.borrowing_price,
            'book':book.title,
            'balance':account.balance
        })
        send_email=EmailMultiAlternatives("Borrow Book", '', to=[request.user.email])
        send_email.attach_alternative(message,"text/html")
        send_email.send()
    else:
        messages.warning(request,"You do not have sufficient balance.")
    return redirect("Home")
def ReturnBookView(request,id):
    borrowed=BorrowModel.objects.get(pk=id)
    borrowed.is_returned=True
    borrowed.save(update_fields=['is_returned'])
    account=request.user.modifieduser
    account.balance+=borrowed.book.borrowing_price
    account.save(update_fields=['balance'])
    return redirect("Profile")
    