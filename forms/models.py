from django.db import models

from enum import Enum

class QuestionType(Enum):   # A subclass of Enum
    MULTIPLE_CHOICE = "Escolha múltima"
    SINGLE_CHOICE = "Escolha única"
    OPEN_QUESTION = "Pergunta de texto aberta"

# Create your models here.

class QuestionTemplate(models.Model):
    pass


class Answer(models.Model):
    question_templates = models.ManyToManyField(QuestionTemplate)
    answer_text = models.CharField(max_length=200)
    answer_type = models.CharField(
      max_length=5,
      choices=[(tag, tag.value) for tag in QuestionType]  # Choices is a list of Tuple
    )
    priority = models.IntegerField(default=0)
