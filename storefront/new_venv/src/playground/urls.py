from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('home/', views.say_hello)
]