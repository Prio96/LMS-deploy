from django.urls import path,include
from .views import BookDetailView
urlpatterns = [
    path('detail/<int:id>',BookDetailView.as_view(),name="BookDetail")
]