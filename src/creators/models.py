from django.contrib.auth import get_user_model
from django.db import models
from letterbox.models import BaseModel


class Creator(get_user_model()):
    pass
    