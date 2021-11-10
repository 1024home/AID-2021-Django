from django.contrib import admin
from .models import Book
from .models import Author


# Register your models here.

class BookManage(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish', 'market_price', 'price']
    list_display_links = ['title']
    search_fields = ['title']


class AuthorManage(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']
    list_display_links = ['name']


admin.site.register(Book, BookManage)
admin.site.register(Author, AuthorManage)
