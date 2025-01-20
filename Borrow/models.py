from django.db import models
from User.models import UserModel
from Book.models import BookModel
# Create your models here.
class BorrowModel(models.Model):
    account=models.ForeignKey(UserModel,related_name='userborrowings',on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,related_name='bookborrowings',on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(auto_now_add=True)
    is_returned=models.BooleanField(default=False)
    balance_after_borrowing=models.DecimalField(max_digits=8,decimal_places=2)
    
    class Meta:
        ordering=['borrow_date']
        

    