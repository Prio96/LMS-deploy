from django.shortcuts import render
from Category.models import CategoryModel
from Book.models import BookModel
def home(request,category_slug=None):
    book=BookModel.objects.all()
    if category_slug is not None:
        category=CategoryModel.objects.get(slug=category_slug)
        book=BookModel.objects.filter(category=category)
    category=CategoryModel.objects.all()
    return render(request,'index.html',{'books':book,'categories':category})