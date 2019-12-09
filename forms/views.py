from django.shortcuts import render
from django.http import HttpResponse

from .models import FormTemplate, FormApplication, QuestionType, Offer, Professor, FormSubmission
import json

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


def form_professor(request, app_id, offer_id, prof_id):
    if request.method == 'GET':
        appl = FormApplication.objects.get(id=app_id)
        offer = Offer.objects.get(id=offer_id)
        prof = Professor.objects.get(id=prof_id)

        questions = [(q.name(offer, prof, appl), q.question_long_text(offer, prof), q) for q in appl.form_template.ordered_questions()]

        return render(request, 'prof.html', { 'questions': questions, 'appl': appl, 'offer': offer, 'prof': prof })
    if request.method == 'POST':

        for k, v in request.POST.items():
            try:
                key = json.loads(k)
                print("decode json", key, v)
                sub = FormSubmission.objects.create(
                    question_type=key['type'],
                    form_application=key['appl__id'],
                    offer=key['offer__id'],
                    prof=key['professor__id'],
                    text_question=key['text'],
                    text_answer=v
                )
                sub.save()

            except json.JSONDecodeError:
                pass


        return render(request, 'answer.html', dict(request.POST.items()))
