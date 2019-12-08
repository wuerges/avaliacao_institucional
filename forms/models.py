from django.db import models

from enum import Enum

class QuestionType(Enum):   # A subclass of Enum
    MC = "Escolha múltipla"
    SC = "Escolha única"
    OQ = "Pergunta de texto aberta"

# Create your models here.

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    answer_type = models.CharField(
      max_length=5,
      choices=[(tag.name, tag.value) for tag in QuestionType]  # Choices is a list of Tuple
    )
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.answer_text, QuestionType[self.answer_type].value)


class QuestionTemplate(models.Model):
    template_name=models.CharField(max_length=200)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.template_name
