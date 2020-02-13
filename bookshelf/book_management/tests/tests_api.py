from django.test import TestCase

from book_management.models import Book


class RestApiTest(TestCase):

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
        Book.objects.create(
            title='Programming Python',
            authors='Kenneth A. Lambert',
            published_date=2010,
            isbn='9781449302856',
            page_count=1632,
            small_thumbnail='https://books.google.com/books/content?id=qtdkAgAAQBAJ&printsec=frontcover&img=1&zoom=5'
                            '&edge=curl&source=gbs_api',
            language='en',
        )

    def test_api_get_all_results(self):
        response = self.client.get('/api/book/')
        count = len(response.json())
        self.assertEquals(count, 2)

    def test_api_filter_title(self):
        response = self.client.get('/api/book/?title=bit')
        count = len(response.json())
        self.assertEquals(count, 1)
        title = response.json()[0]['title']
        self.assertEquals(title, 'Hobbit czyli Tam i z powrotem')

    def test_api_filter_pub_date_gt(self):
        response = self.client.get('/api/book/?published__gt=2006')
        count = len(response.json())
        self.assertEquals(count, 1)
        pub_date = response.json()[0]['published_date']
        self.assertEquals(pub_date, 2010)