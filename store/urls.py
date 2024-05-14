
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='prodcuts')
router.register('collections', views.CollectionViewSet)

# nested-review URL
products_routers = routers.NestedDefaultRouter(
    router, 'products', lookup='product')

products_routers.register(
    'reviews', views.ReviewViewSet, basename='product-review')


# URL configuration
urlpatterns = router.urls + products_routers.urls


# urlpatterns = [
#     path("products/", views.ProductList.as_view()),
#     path("products/<int:pk>/", views.ProductDetail.as_view()),
#     path("collections/", views.CollectionList.as_view()),
#     path("collections/<int:pk>/", views.ColllectionDetail.as_view()),
#     path("__debug__/", include("debug_toolbar.urls")),

# ]
