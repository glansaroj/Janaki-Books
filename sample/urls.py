
from django.urls import path, include
from . import views


# URL configuration
urlpatterns = [
    path('namaste/', views.greet),
    path("__debug__/", include("debug_toolbar.urls")),


]
