from django.test import TestCase

from book_management.models import Book


class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(
            title='Hobbit czyli Tam i z powrotem',
            authors='J. R. R. Tolkien',
            published_date=2004,
            isbn='8320717507',
            page_count=315,
            small_thumbnail='https://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=5'
                            '&source=gbs_api',
            language='en',
        )

    def test_book_content(self):
        book = Book.objects.get(id=1)
        expected_title = book.title
        self.assertEquals(expected_title, 'Hobbit czyli Tam i z powrotem')
