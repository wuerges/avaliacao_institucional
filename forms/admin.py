from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header = 'Monty Python administration'

my_admin_site = MyAdminSite(name='myadmin')


# Register your models here.
from .models import Answer, QuestionTemplate, Question, Professor, \
    Semester, Major, Offer, Course, Professor, FormTemplate, \
        FormApplication, Profile

my_admin_site.register(Answer)
my_admin_site.register(QuestionTemplate)
my_admin_site.register(Question)
my_admin_site.register(Semester)
my_admin_site.register(Major)
my_admin_site.register(Offer)
my_admin_site.register(Course)
my_admin_site.register(Professor)
my_admin_site.register(FormTemplate)
my_admin_site.register(FormApplication)
my_admin_site.register(Profile)
