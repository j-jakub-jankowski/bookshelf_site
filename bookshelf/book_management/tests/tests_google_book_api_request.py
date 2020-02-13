from django.test import TestCase

from book_management.googlebooksapi import get_books


class GoogleBookApiTest(TestCase):
    def setUp(self):
        params = {'q': 'hobbit', 'intitle': 'hobbit'}
        start_index = 0
        self.results_1 = get_books(params, start_index)

        params = {'q': 'hobbit', 'isbn': '9780547951973'}
        start_index = 0
        self.results_2 = get_books(params, start_index)

    def test_results_contains_param(self):
        for book in self.results_1['search_result']:
            if 'hobbit' in book['volumeInfo']['title'][0]:
                contains = True
                self.assertTrue(contains)

    def test_results_contains_one_book(self):
        book_count = self.results_2['total_items']
        self.assertEquals(book_count, 1)
