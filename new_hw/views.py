from django.shortcuts import render
from .models import Author, Publisher, Book, Store
from django.db.models import Avg, Count



def book_view(request):

    # book_list = Book.objects.prefetch_related('authors').values('id', 'name', 'authors__name')
    book_list = Book.objects.prefetch_related('authors')

    return render(request, 'new_hw/book_view.html',
                  {'book_list': book_list})


def detail_book_view(request, pk):

    book = Book.objects.select_related('publisher').prefetch_related('authors').get(pk=pk)

    return render(request, 'new_hw/detail_book_view.html',
                  {'book': book})


def author_detail_view(request, pk):
    # author = Author.objects.get(pk=pk)
    author = Author.objects.prefetch_related("book_set").get(pk=pk)
    return render(request, "new_hw/author_detail_view.html", {'author': author})

def store_view(request, pk):

    store_list = Store.objects.prefetch_related('books__authors').\
        values('books__price', 'books__rating','books__authors__name', 'books__name', 'name').filter(pk=pk)
    store_name = Store.objects.values('name').get(pk=pk)
    return render(request, 'new_hw/store_view.html', {'store_list': store_list, 'store_name': store_name})


def random_things_view(request):
    x = Store.objects.annotate(av_pr=Avg('books__price'), av_r=Avg('books__rating'), count=Count('books'))
    averge_price = []
    for i in x:
        averge_price.append({'name': i.name, "av_pr": int(i.av_pr), 'av_r': int(i.av_r), 'count': i.count})

    return render(request, 'new_hw/random_things_view.html', {'averge_price': averge_price})
