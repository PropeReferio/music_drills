from django.urls import path

from . import views

app_name = 'getdrills'

urlpatterns = [
    path("", views.index, name="index"),
    path("drills/all", views.all_drills, name="all_drills"),
    path("drills", views.random_drills_by_int, name="random_drills_by_int"),
    path("drills_by_cat", views.random_drills_by_int_and_category, name="random_drills_by_int_and_category"),
]
