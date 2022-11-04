from django.urls import path

from . import views #şu an ki dosya'dan views'ü içe aktar

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="Anasayfam"),
    path("create/", views.create, name="create"),
]