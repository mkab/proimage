from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    image_url = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)

    class Meta:
        model = Image
        fields = [
            "uuid",
            "name",
            "image_url",
            "description",
        ]

    def save(self, **kwargs):
        if self.instance and self.instance.image_url:
            self.instance.image_url.delete()
        return super().save(**kwargs)
