from django.db.models import Avg, Count
from django.shortcuts import render

from .models import Author, Book, Store


def book_view(request):

    book_list = Book.objects.prefetch_related('authors')

    return render(request, 'new_hw/book_view.html',
                  {'book_list': book_list})


def detail_book_view(request, pk):

    book = Book.objects.select_related('publisher').prefetch_related('authors').get(pk=pk)

    return render(request, 'new_hw/detail_book_view.html',
                  {'book': book})


def author_detail_view(request, pk):

    author = Author.objects.prefetch_related("book_set").get(pk=pk)
    return render(request, "new_hw/author_detail_view.html", {'author': author})


def store_view(request, pk):

    store_list = Store.objects.prefetch_related('books__authors').\
        values('books__price', 'books__rating', 'books__authors__name',
               'books__name', 'name').filter(pk=pk)
    store_name = Store.objects.values('name').get(pk=pk)
    return render(request, 'new_hw/store_view.html',
                  {'store_list': store_list, 'store_name': store_name})


def random_things_view(request):
    stores = Store.objects.annotate(av_pr=Avg('books__price'),
                                    av_r=Avg('books__rating'), count=Count('books'))
    random_staff = []
    for store in stores:
        random_staff.append({'name': store.name, "av_pr": int(store.av_pr),
                             'av_r': int(store.av_r), 'count': store.count})

    return render(request, 'new_hw/random_things_view.html',
                  {'random_staff': random_staff})
