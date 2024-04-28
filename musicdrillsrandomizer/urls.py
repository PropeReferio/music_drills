from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("getdrills/", include("getdrills.urls")),
    path("admin/", admin.site.urls),
]
