from django.urls import path
from .views import *

from .views import main,detail_pro

urlpatterns = [
    path("", main, name="home"),
    path("details/<int:id>",detail_pro, name="details"),
    path("search/", main, name='search')
]
