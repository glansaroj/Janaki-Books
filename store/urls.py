
from django.urls import path, include
from . import views


# URL configuration
urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>/", views.product_detail),
    path("__debug__/", include("debug_toolbar.urls")),

]
