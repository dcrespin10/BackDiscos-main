from django.urls import path
from .views import DiscosAllViewset

urlpatterns = [
    path('api/listar_discos/', DiscosAllViewset.as_view()),
]