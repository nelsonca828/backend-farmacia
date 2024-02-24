from rest_framework.pagination import PageNumberPagination

class smallSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_size = 10

class mediumSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_size = 50

class largeSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_size = 100