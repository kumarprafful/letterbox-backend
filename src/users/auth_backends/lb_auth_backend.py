from django.contrib.auth.backends import ModelBackend
from letterbox.exceptions import LBException
from users.models import User
from users.utils import fetch_google_user_info

class LBAuthBackend(ModelBackend):

    def get_authenticated_user_from_email(self, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if not (self.user_can_authenticate(user)):
            return None
        return user

    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        user = super(LBAuthBackend, self).authenticate(request, username, password)

        if user is None and hasattr(request, 'data') and request.data.get('token'):
            token = request.data.get('token')
            user = self.google_oauth(token)

        elif user is None and password:
            user = self.get_authenticated_user_from_email(email=username)
            if not user.check_password(password):
                return None
        return user

    def google_oauth(self, token):
        user_info = fetch_google_user_info(token)

        if user_info is None:
            raise LBException('G-user not found')

        email = user_info.get('email')

        user = self.get_authenticated_user_from_email(email=email)
        return user
