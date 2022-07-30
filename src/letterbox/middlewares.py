from django.conf import settings
from django.utils.timezone import activate, deactivate


class TimeZoneMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        user_timezone = settings.DEFAULT_TIMEZONE
        activate(user_timezone)
        response = self.get_response(request)
        deactivate()
        return response
