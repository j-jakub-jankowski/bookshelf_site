from django.test import TestCase

from book_management.forms import BookForm


class AddBookFormTest(TestCase):

    def test_form_is_valid(self):
        form_data = {
            'title': 'Hobbit czyli Tam i z powrotem',
            'authors': 'J. R. R. Tolkien',
            'published_date': 2004,
            'isbn': '8320717507',
            'page_count': 315,
            'small_thumbnail': 'https://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=5'
                               '&source=gbs_api',
            'language': 'en',
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_pub_date_invalid(self):
        form_data = {
            'title': 'Hobbit czyli Tam i z powrotem',
            'authors': 'J. R. R. Tolkien',
            'published_date': 1000,
            'isbn': '8320717507',
            'page_count': 315,
            'small_thumbnail': 'https://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=5'
                               '&source=gbs_api',
            'language': 'en',
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_page_count_invalid(self):
        form_data = {
            'title': 'Hobbit czyli Tam i z powrotem',
            'authors': 'J. R. R. Tolkien',
            'published_date': 2004,
            'isbn': '8320717507',
            'page_count': -2,
            'small_thumbnail': 'https://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=5'
                               '&source=gbs_api',
            'language': 'en',
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())