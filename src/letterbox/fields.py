from django.db import models
from django.core.validators import RegexValidator

from letterbox.utils.random import random_alpha_id


class IdentifierField(models.SlugField):
    default_validators = [RegexValidator(
        r'^[0-9a-zA-Z\-]+$', 'Name can only have digits, dashes and lower case alphabets')]

    def __init__(self, allow_uppercase=True, *args, **kwargs):
        if allow_uppercase:
            self.default_validators = [RegexValidator(
                r'^[0-9a-zA-Z\-\_]+$', 'Name can only have digits, dashes and alphabets')]

        super().__init__(max_length=kwargs.pop("max_length", 255),
                         unique=kwargs.pop("unique", True),
                         help_text=kwargs.pop("help_text", "internal name"),
                         db_index=True, *args, **kwargs)
