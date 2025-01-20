from django.db import models
from django.contrib.auth.models import User
from Book.models import BookModel

# Create your models here.
class UserModel(models.Model):
    user=models.OneToOneField(User,related_name='modifieduser',on_delete=models.CASCADE)
    balance=models.DecimalField(max_digits=8,decimal_places=2,default=0)#usermodel_object.baseuser.balance

    def __str__(self):
        return self.user.username
    
class DepositModel(models.Model):
    account=models.ForeignKey(UserModel,related_name='deposits',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self):
        return f"{self.account.user.username} deposited ${self.amount}"
    

class ReviewModel(models.Model):
    account=models.ForeignKey(UserModel,related_name='user_reviews',on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,related_name='book_reviews',on_delete=models.CASCADE)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review on {self.book.title} by {self.account.user.username}"

    

    
    