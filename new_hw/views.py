from django.shortcuts import render
from django.views import generic
from .models import Author, Publisher, Book, Store




def book_view(request):

    book_list = Book.objects.values('name', 'authors__name', 'id')

    return render(request, 'new_hw/book_view.html',
                  {'book_list': book_list})


def detail_book_view(request, pk):

    book = Book.objects.select_related('publisher').prefetch_related('authors').get(pk=pk)
    '''
    Есть вопрос
    Почему стоит использовать select_related и prefetch_related, если
    book = Book.objects.filter(id=pk).values('name', 'pages', 'price', 'rating', 'pubdate', 'authors__name', 'publisher__name', 'pubdate')
    работает быстрее? 
    '''

    return render(request, 'new_hw/detail_book_view.html',
                  {'book': book})


def author_detail_view(request, pk):
    # author = Author.objects.get(pk=pk)
    author = Author.objects.prefetch_related("book_set").get(pk=pk)
    return render(request, "new_hw/author_detail_view.html", {'author': author})


