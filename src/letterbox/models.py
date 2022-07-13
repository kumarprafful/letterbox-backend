import uuid

from django.db import models

from letterbox.fields import IdentifierField


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = IdentifierField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
