from django.urls import path

from .views import contact_as_view


urlpatterns = [
    path('contact/', contact_as_view, name='contact'),
]
