from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preview/<int:form_template_id>', views.form_preview, name='preview'),
    path('links/<int:form_application_id>', views.form_links, name='links')
]

