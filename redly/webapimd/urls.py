from django.urls import include, path

from . import views

urlpatterns = [
    path('ini/', views.home),
    path('cre/', views.cad),
    path('getposts/<int:lsd>/',views.gtPost),
    path('getposts/',views.gtPost),
    path('postposts/',views.ptPost),
]
