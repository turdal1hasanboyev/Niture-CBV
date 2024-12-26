from django.urls import path

from .views import login_as_view, logout_as_view, register_as_view


urlpatterns = [
    path('login/', login_as_view, name='login'),
    path('logout/', logout_as_view, name='logout'),
    path('register/', register_as_view, name='register'),  
]
