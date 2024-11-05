from rest_framework.pagination import PageNumberPagination

class SmallSetPagination(PageNumberPagination):
    page_query_params = 'p'
    page_size = 6
    page_size_query_params = 'page_size'
    max_page_size = 6

class MediumSetPagination(PageNumberPagination):
    page_query_params = 'p'
    page_size = 9
    page_size_query_params = 'page_size'
    max_page_size = 9

class LargeSetPagination(PageNumberPagination):
    page_query_params = 'p'
    page_size = 18
    page_size_query_params = 'page_size'
    max_page_size = 18