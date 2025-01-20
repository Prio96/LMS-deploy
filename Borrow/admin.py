from django.contrib import admin
from .models import BorrowModel
# Register your models here.

@admin.register(BorrowModel)
class BorrowAdmin(admin.ModelAdmin):
    list_display=['account','book','borrow_date','balance_after_borrowing','is_returned']