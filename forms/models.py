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


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    priority = models.IntegerField(default=1)
    question_template = models.ForeignKey(QuestionTemplate, on_delete=models.PROTECT)

    def __str__(self):
        return "{}: {}".format(self.priority, self.question_text)

class FormTemplate(models.Model):
    name = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Offer(models.Model):
    professors = models.ManyToManyField(Professor)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} - {}".format(self.course, ", ".join(p.name for p in self.professors))

class Major(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=200)
    semester = models.ManyToManyField(Offer)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {} {}".format(self.major.name, self.name)






    