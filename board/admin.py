from django.contrib import admin
from .models import Board
# Register your models here.
#신청목록
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'content'
        )
    search_fields = (
        'user',
        'title',
        'content'
        )
    list_filter = (
        'user',
        'title',
        'content'
        )