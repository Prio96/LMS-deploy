from django import forms
from User.models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model=ReviewModel
        fields=['content']