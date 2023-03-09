from django.views import generic
from django.db.models import Avg, Count
from django.shortcuts import render

from .models import Author, Book, Store, Publisher


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
        return Publisher.objects.all()

class PublisherDetailView(generic.DetailView):
    model = Publisher
    template_name = 'new_hw/publisher_detail_view.html'

class StoreListView(generic.ListView):
    model = Store
    template_name = 'new_hw/store_list_view.html'

    def get_queryset(self):
        return Store.objects.all()

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'new_hw/store_detail_view.html'



# def book_view(request):
#
#     book_list = Book.objects.prefetch_related('authors')
#
#     return render(request, 'new_hw/book_list_view.html',
#                   {'book_list': book_list})
#
#
# def detail_book_view(request, pk):
#
#     book = Book.objects.select_related('publisher').prefetch_related('authors').get(pk=pk)
#
#     return render(request, 'new_hw/book_detail_view.html',
#                   {'book': book})
#
#
# def author_detail_view(request, pk):
#
#     author = Author.objects.prefetch_related("book_set").get(pk=pk)
#     return render(request, "new_hw/author_detail_view.html", {'author': author})
#
#
# def store_view(request, pk):
#
#     store_list = Store.objects.prefetch_related('books__authors').\
#         values('books__price', 'books__rating', 'books__authors__name',
#                'books__name', 'name').filter(pk=pk)
#     store_name = Store.objects.values('name').get(pk=pk)
#     return render(request, 'new_hw/store_view.html',
#                   {'store_list': store_list, 'store_name': store_name})
#
#
# def random_things_view(request):
#     stores = Store.objects.annotate(av_pr=Avg('books__price'),
#                                     av_r=Avg('books__rating'), count=Count('books'))
#     random_staff = []
#     for store in stores:
#         random_staff.append({'name': store.name, "av_pr": int(store.av_pr),
#                              'av_r': int(store.av_r), 'count': store.count})
#
#     return render(request, 'new_hw/random_things_view.html',
#                   {'random_staff': random_staff})
