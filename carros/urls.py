from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarroViewSet

router = DefaultRouter()
router.register(r'carros', CarroViewSet, basename='carro')

urlpatterns = [
    path('', include(router.urls)),
]
