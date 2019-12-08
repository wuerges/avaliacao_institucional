from django.db import models

from enum import Enum

class QuestionType(Enum):   # A subclass of Enum
    MULTIPLE_CHOICE = "Escolha múltipla"
    SINGLE_CHOICE = "Escolha única"
    OPEN_QUESTION = "Pergunta de texto aberta"

# Create your models here.

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    answer_type = models.CharField(
      max_length=5,
      choices=[(tag, tag.value) for tag in QuestionType]  # Choices is a list of Tuple
    )
    priority = models.IntegerField(default=0)


class QuestionTemplate(models.Model):
    template_name=models.CharField(max_length=200)
    answers = models.ManyToManyField(Answer)