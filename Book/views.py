from django.shortcuts import render
from django.views.generic import DetailView
from .models import BookModel
from .forms import ReviewForm
from Borrow.models import BorrowModel
# Create your views here.
class BookDetailView(DetailView):
    model=BookModel
    pk_url_kwarg='id'
    template_name='book_detail.html'
    
    def post(self, request, *args, **kwargs):
        book=self.get_object()
        review_form=ReviewForm(data=self.request.POST)
        if review_form.is_valid():
            review=review_form.save(commit=False)
            review.book=book
            review.account=self.request.user.modifieduser
            review_form.save()
            return self.get(request,*args,**kwargs)
        
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        book=self.get_object()
        reviews=book.book_reviews.all()
        review_form=ReviewForm()
        if self.request.user.is_authenticated:
            has_read=BorrowModel.objects.filter(account=self.request.user.modifieduser,book=book).exists()
            context['has_read']=has_read
            context['reviews']=reviews
            context['review_form']=review_form
            context['book']=book
            return context
        else:
            context['reviews']=reviews
            context['book']=book
            return context