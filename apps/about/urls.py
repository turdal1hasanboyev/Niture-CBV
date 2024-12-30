from django.urls import path

from . import views


urlpatterns = [
    path('about/', views.about_as_view, name='about'),
]
