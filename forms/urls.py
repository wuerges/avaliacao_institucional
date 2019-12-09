from django.urls import path

from . import views

from .admin import my_admin_site

urlpatterns = [
    path('admin/', my_admin_site.urls),
    path('', views.index, name='index'),
]

