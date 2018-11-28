from django.urls import include, path

from . import views

urlpatterns = [
    path(r'ini/', views.home),
    path(r'cre/', views.cad),
    path(r'getposts/<int:lsd>/',views.gtPost),
    path(r'postposts/',views.ptPost),
]
