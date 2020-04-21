from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pages.api.viewsets import PageViewSet


router = routers.DefaultRouter()
router.register('pages', PageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
