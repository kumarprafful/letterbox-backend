from rest_framework.pagination import CursorPagination as CPagination


class LBPagination(CPagination):
    page_size = 50
    ordering = '-created_at'
