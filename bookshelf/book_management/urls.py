from django.urls import path

from . import views

urlpatterns = [
    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('add/', views.AddBookView.as_view(), name='add'),
    path('import/<int:start_index>/', views.ImportBookView.as_view(), name='import'),
    path('import_all/', views.import_all, name='import_all'),
    path('', views.BookListView.as_view(), name='list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail')
]
