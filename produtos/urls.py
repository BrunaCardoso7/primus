from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutosViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutosViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
]
