from django.urls import include, path
from rest_framework import routers

from proimage import views

router = routers.DefaultRouter()
router.register("image", views.ImageUploadViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
