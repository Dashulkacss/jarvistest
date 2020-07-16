from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name = 'contacts'),
    path('create', views.create, name = 'create')
]