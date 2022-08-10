import uuid

from django.db import models
from model_utils.models import TimeStampedModel


def upload_path(instance, filename):
    return f"images/{instance.uuid}/{filename}"


class Image(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to=upload_path)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created"]
