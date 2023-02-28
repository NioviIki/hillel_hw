from django.urls import path
from . import views

app_name = 'new_hw'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),

urlpatterns = [
    path('book/', views.book_view, name='book'),
    path('book/<int:pk>', views.detail_book_view, name='detail'),
    path('author/<int:pk>', views.author_detail_view, name='author_detail')
]