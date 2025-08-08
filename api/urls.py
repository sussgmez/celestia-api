from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet, CurrentUserView, OrderViewSet, CategoryViewSet, ProductSizeViewSet, ProductImageViewSet, ProductVariantViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'productvariants', ProductVariantViewSet)
router.register(r'productimages', ProductImageViewSet)
router.register(r'productsizes', ProductSizeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user/', CurrentUserView.as_view(), name='current_user'),
] 