from django.urls import path

from .views import home_page_as_view


urlpatterns = [
    path('', home_page_as_view, name='home'),
]
