from django.urls import include, path

from . import views

urlpatterns = [
    path(r'redly/', views.redhome,name='home'),
    path(r'redly/redid/<int:id>/', views.removeChat,name='delChat'),

    # path('redly/pt/d/', views.sendChat,name='chat'),

]
