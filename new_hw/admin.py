from django.contrib import admin

from .models import Author, Book, Publisher, Store


class BookPublisherInline(admin.TabularInline):
    model = Book
    extra = 1


class BookStoreInline(admin.TabularInline):
    model = Store.books.through
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ['name', 'age']
    list_filter = ['age']
    list_per_page = 20


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_per_page = 20
    search_fields = ['name']
    inlines = [BookPublisherInline, ]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [BookStoreInline, ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'rating', 'author')
    list_filter = ('rating', 'authors')
    search_fields = ('name', 'author')
