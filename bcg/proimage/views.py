from rest_framework import permissions, status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Image
from .serializers import ImageSerializer


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    lookup_field = "uuid"

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            image_uuid = data["uuid"]
            return Response(
                data={
                    "image_uuid": image_uuid,
                    "message": "Image saved successfully",
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
