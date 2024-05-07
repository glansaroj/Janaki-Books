
from django.contrib import admin
from django.urls import path, include
import debug_toolbar


admin.site.site_header = "Janaki Books Admin"
admin.site.index_title = "Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', include('sample.urls')),
    path('store/', include('store.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
