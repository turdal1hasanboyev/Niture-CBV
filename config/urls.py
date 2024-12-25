"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin # admin
from django.urls import path, include, re_path # default

# for media and static files
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

# page not found
# from django.conf.urls import handler404
# from .errors import page_not_found_as_view
# from .errors import PageNotFoundView


urlpatterns = [
    path('niture/', admin.site.urls), # admin

    # ckeditor path
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # for media and static files
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # local path
    path('', include('apps.product.urls')),
    path('about/', include('apps.about.urls')),
    path('blog/', include('apps.blog.urls')),
    path('common/', include('apps.common.urls')),
    path('user/', include('apps.user.urls')),
    path('contact/', include('apps.contact.urls')),
]

# for DEBUG

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'config.errors.page_not_found_as_view'
