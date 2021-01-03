from django.urls import path
from .views import Opinion, Lista


urlpatterns = [
    path('', Opinion.as_view(), name="home"),
    path('lista', Lista.as_view() , name="lista"),
]