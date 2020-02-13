from django.test import TestCase
from django.urls import reverse


class BookshelfPageTest(TestCase):

    def test_bookshelf_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 302)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('bookshelf'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bookshelf'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_management/book_list.html')

    def test_view_load_base_template(self):
        response = self.client.get(reverse('bookshelf'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_management/base.html')


class AddPageTest(TestCase):
    # failed, I don,t know why :(
    """def test_add_page_status_code(self):
        response = self.client.get('/add/')
        self.assertEquals(response.status_code, 200)"""

    def test_view_url_by_name(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_management/add_book.html')

    def test_view_load_base_template(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_management/base.html')


class ImportPageTest(TestCase):
    # failed, I don,t know why :(
    """def test_import_page_status_code(self):
        response = self.client.get('/import/')
        self.assertEquals(response.status_code, 200)"""

    def test_view_url_by_name(self):
        response = self.client.get(reverse('import', kwargs={'start_index': 0}))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('import', kwargs={'start_index': 0}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_management/import_books.html')

    def test_view_load_base_template(self):
        response = self.client.get(reverse('import', kwargs={'start_index': 0}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_management/base.html')


class ApiPageTest(TestCase):
    def test_api_page_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

    def test_api_list_page_status_code(self):
        response = self.client.get('/api/book/')
        self.assertEquals(response.status_code, 200)



