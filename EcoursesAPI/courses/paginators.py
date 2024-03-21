from rest_framework import pagination
from . import models

class CoursesPaginator(pagination.PageNumberPagination):
    page_size = 5