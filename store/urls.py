
from django.urls import path, include
from . import views


# URL configuration
urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>/", views.product_detail),
    path("collections/", views.CollectionList.as_view()),
    path("collections/<int:id>/", views.CollectionDetail.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),

]
