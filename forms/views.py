from django.shortcuts import render
from django.http import HttpResponse

from .models import FormTemplate, FormApplication, QuestionType

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def form_preview(request, form_template_id):
    if request.method == 'GET':
        try:
            tmpl = FormTemplate.objects.get(id=form_template_id)
        except FormTemplate.DoesNotExist:
            raise Http404("form does not exist.")
        return render(request, 'preview.html', {'tmpl': tmpl})

    if request.method == 'POST':
        print(request)
        return render(request, 'answer.html', {})


def form_links(request, form_application_id):

    appl = FormApplication.objects.get(id=form_application_id)
    offers = appl.semester.offer.all()

    courses = []
    for off in offers:
        courses.append((appl, off, off.course))

    profs = []
    for off in offers:
        for p in off.professors.all():
            profs.append((appl, off, p))


    return render(request, 'links.html', { 'appl': appl, 'courses': courses, 'profs': profs })