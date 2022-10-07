
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("search/<str:word>/",views.search,name="search"),
    path("json_response/<str:word>/",views.json_response,name="json_response")
]

