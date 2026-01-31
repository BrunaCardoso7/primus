from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SugestaoViewSet

router = DefaultRouter()
router.register(r'usuarios', SugestaoViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]
