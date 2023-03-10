from django.db.models import Count
from django.views import generic

from .models import Author, Book, Publisher, Store


class AuthoLlistView(generic.ListView):
    model = Author
    template_name = 'new_hw/author_list_view.html'

    def get_queryset(self):
        return Author.objects.annotate(c=Count('book')).prefetch_related('book_set')


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'new_hw/author_detail_view.html'

    def get_queryset(self):
        return Author.objects.prefetch_related('book_set')


class BookListView(generic.ListView):
    model = Book
    template_name = 'new_hw/book_list_view.html'

    def get_queryset(self):
        return Book.objects.values('id', 'name')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'new_hw/book_detail_view.html'

    def get_queryset(self):
        return Book.objects.prefetch_related('authors', 'publisher')


class PublisherListView(generic.ListView):
    model = Publisher
    template_name = 'new_hw/publisher_list_view.html'

    def get_queryset(self):
        return Publisher.objects.prefetch_related('book_set')


class PublisherDetailView(generic.DetailView):
    model = Publisher
    template_name = 'new_hw/publisher_detail_view.html'

    def get_queryset(self):
        return Publisher.objects.prefetch_related('book_set')


class StoreListView(generic.ListView):
    model = Store
    template_name = 'new_hw/store_list_view.html'

    def get_queryset(self):
        return Store.objects.prefetch_related('books')


class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'new_hw/store_detail_view.html'
