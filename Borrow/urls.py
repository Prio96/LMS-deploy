from django.urls import path,include
from . import views
urlpatterns = [
    path('borrow/<int:id>',views.BorrowBookView,name="BorrowBook"),
    path('return/<int:id>',views.ReturnBookView,name="ReturnBook"),
]