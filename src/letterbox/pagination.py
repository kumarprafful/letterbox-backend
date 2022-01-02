from rest_framework.pagination import CursorPagination as CPagination


class CursorPagination(CPagination):
    page_size = 50
    ordering = '-created_at'
