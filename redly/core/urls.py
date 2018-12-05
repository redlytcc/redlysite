from django.urls import include, path

from . import views

urlpatterns = [
    path(r'login/', views.log,name='login'),
    path(r'', views.homeinit,name='index'),
    path(r'create/',views.cada,name='create'),
    path(r'off/',views.offline,name="offline"),
    path(r'final/',views.outred,name='logout'),

]
