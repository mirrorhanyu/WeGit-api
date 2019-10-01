import unittest

from helpers.common.pagination import get_max_page


class PaginationTest(unittest.TestCase):

    def test_should_return_0_when_header_is_none(self):
        self.assertEqual(get_max_page(None), 0)

    def test_should_return_34_when_current_page_in_header_is_9(self):
        link = '<https://api.github.com/search/repositories?q=996&page=8>; rel="prev",' \
               '<https://api.github.com/search/repositories?q=996&page=10>; rel="next", ' \
               '<https://api.github.com/search/repositories?q=996&page=34>; rel="last", ' \
               '<https://api.github.com/search/repositories?q=996&page=1>; rel="first"'
        self.assertEqual(get_max_page(link), 34)

    def test_should_return_34_when_current_page_in_header_is_the_first_page(self):
        link = '<https://api.github.com/search/repositories?q=996&page=2>; rel="next", ' \
               '<https://api.github.com/search/repositories?q=996&page=34>; rel="last"'
        self.assertEqual(get_max_page(link), 34)

    def test_should_return_34_when_current_page_in_header_is_the_last_page(self):
        link = '<https://api.github.com/search/repositories?q=996&page=33>; rel="prev", ' \
               '<https://api.github.com/search/repositories?q=996&page=1>; rel="first"'
        self.assertEqual(get_max_page(link), 34)
