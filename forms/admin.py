from django.contrib import admin

# Register your models here.
from .models import Answer, QuestionTemplate, Question

admin.site.register(Answer)
admin.site.register(QuestionTemplate)
admin.site.register(Question)

