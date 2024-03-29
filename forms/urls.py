from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preview/<int:form_template_id>', views.form_preview, name='preview'),
    path('record/<int:app_id>/<int:offer_id>/<int:prof_id>', views.form_record, name='record'),
    path('report/<int:app_id>/<int:offer_id>/<int:prof_id>', views.form_report, name='report'),
    path('links/<int:form_application_id>', views.form_links, name='links')
]

