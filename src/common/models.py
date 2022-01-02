from django.db import models

from letterbox.fields import IdentifierField


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(
    # 'users.User', on_delete=models.SET_NULL, null=True, editable=False, auto_created=True, related_name='created_by_user')

    class Meta:
        abstract = True


class Tag(TimeStampedModel):
    name = IdentifierField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
