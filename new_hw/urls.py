from django.urls import path

from . import views

app_name = 'new_hw'

urlpatterns = [
    path('author/', views.AuthoLlistView.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('publisher/', views.PublisherListView.as_view(), name='publisher_list'),
    path('publisher/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_detail'),  # noqa:E501
    path('store/', views.StoreListView.as_view(), name='store_list'),
    path('store/<int:pk>/', views.StoreDetailView.as_view(), name='store_detail')
]
