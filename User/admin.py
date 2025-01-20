from django.contrib import admin
from .models import UserModel, DepositModel, ReviewModel
# Register your models here.
admin.site.register(UserModel)
admin.site.register(DepositModel)
admin.site.register(ReviewModel)
