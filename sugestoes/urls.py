from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SugestaoViewSet

router = DefaultRouter()
router.register(r'sugestoes', SugestaoViewSet, basename='sugestao')

urlpatterns = [
    path('', include(router.urls)),
]
