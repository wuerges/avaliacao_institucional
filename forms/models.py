from django.db import models

from enum import Enum

class AnswerType(Enum):   # A subclass of Enum
    MC = "Escolha múltipla"
    SC = "Escolha única"
    OQ = "Pergunta de texto aberta"

class QuestionType(Enum):   # A subclass of Enum
    GERAL = "Pergunta geral sobre a instituição"
    CURSO = "Pergunta geral do curso"
    DISC = "Pergunta para disciplinas"
    PROF = "Pergunta para professor"
    COORD = "Pergunta para coordenação"

from django.contrib.auth.models import User

class Major(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User, related_name='major')
    # user = models.ForeignKey(User, related_name='major', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# Create your models here.

class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    answer_type = models.CharField(
      max_length=5,
      choices=[(tag.name, tag.value) for tag in AnswerType]  # Choices is a list of Tuple
    )
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.answer_text, AnswerType[self.answer_type].value)


class QuestionTemplate(models.Model):
    template_name=models.CharField(max_length=200)
    answers = models.ManyToManyField(Answer)
    question_type = models.CharField(
      max_length=5,
      choices=[(tag.name, tag.value) for tag in QuestionType]  # Choices is a list of Tuple
    )

    def __str__(self):
        return "{} ({})".format(self.template_name,  QuestionType[self.question_type].value)


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

    def ordered_questions(self):
        return self.questions.order_by('priority')

class Professor(models.Model):
    name = models.CharField(max_length=200)
    major = models.ManyToManyField(Major, related_name='professors')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    major = models.ManyToManyField(Major)

    def __str__(self):
        return self.name


class Offer(models.Model):
    professors = models.ManyToManyField(Professor)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} - {}".format(self.course.name, ", ".join(p.name for p in self.professors.all()))
        # return "{} - ".format(self.course.name)


class Semester(models.Model):
    name = models.CharField(max_length=200)
    offer = models.ManyToManyField(Offer)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.major.name, self.name)


class FormApplication(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    form_template = models.ForeignKey(FormTemplate, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.semester, self.form_template)


