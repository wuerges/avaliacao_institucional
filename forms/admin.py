from django.contrib import admin

# Register your models here.
from .models import Answer, QuestionTemplate

admin.site.register(Answer)
admin.site.register(QuestionTemplate)

