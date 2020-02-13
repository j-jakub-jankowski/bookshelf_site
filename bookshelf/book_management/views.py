from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic import View

from .filters import BookFilter
from .forms import BookForm, GoogleBookApiForm
from .googlebooksapi import get_books
from .models import Book


def bookshelf(request):
    print(request)
    """list of books in database with possibility of filtering"""
    book_list_all = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list_all)
    return render(request, 'book_management/book_list.html', {'filter': book_filter})


class AddBookView(View):
    """add single book to database"""

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return render(request, 'book_management/add_book.html', {'form': form, 'book': book})
        else:
            return render(request, 'book_management/add_book.html', {'form': form})

    def get(self, request):
        form = BookForm()
        return render(request, 'book_management/add_book.html', {'form': form})


class ImportBookView(View):
    """import books from Google Books Api and save to database"""

    def post(self, request, start_index):
        form = GoogleBookApiForm

        params = request.POST
        result = get_books(params, start_index)
        request.session['result_to_save'] = result['search_result']

        return render(request, 'book_management/import_books.html',
                      {'form': form, 'search_result': result['search_result'], 'start_index': start_index,
                       'total_items': result['total_items']})

    def get(self, request, start_index):
        form = GoogleBookApiForm
        return render(request, 'book_management/import_books.html',
                      {'form': form})


def import_all(request):
    result_to_save = request.session['result_to_save']

    for book in result_to_save:
        try:
            authors = '; '
            authors = authors.join(book['volumeInfo']['authors'])

            new_book = Book.objects.create(
                title=book['volumeInfo']['title'],
                authors=authors,
                published_date=book['volumeInfo']['publishedDate'][:4],
                isbn=book['volumeInfo']['industryIdentifiers'][0]['identifier'],
                page_count=book['volumeInfo']['pageCount'],
                small_thumbnail=book['volumeInfo']['imageLinks']['smallThumbnail'],
                language=book['volumeInfo']['language']
            )
            new_book.save()
        except KeyError:
            pass

    return redirect('/book/import/0/')


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
