from django.contrib import admin

# Register your models here.
from .models import Answer, QuestionTemplate, Question, Professor, \
    Semester, Major, Offer, Course, Professor, FormTemplate

admin.site.register(Answer)
admin.site.register(QuestionTemplate)
admin.site.register(Question)
admin.site.register(Semester)
admin.site.register(Major)
admin.site.register(Offer)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(FormTemplate)
