from django.db import models
from Category.models import CategoryModel
# Create your models here.
class BookModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='Book/media/uploads')
    borrowing_price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ManyToManyField(CategoryModel)
    
    def __str__(self):
        return self.title