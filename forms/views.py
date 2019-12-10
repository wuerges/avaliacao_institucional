from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict 
import pandas as pd
import tempfile as tf

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


def form_record(request, app_id, offer_id, prof_id):
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
                    form_application=FormApplication.objects.get(id=key['appl__id']),
                    offer=Offer.objects.get(id=key['offer__id']),
                    professor=Professor.objects.get(id=key['professor__id']),
                    text_question=key['text'],
                    text_answer=v
                )
                sub.save()

            except json.JSONDecodeError:
                pass


        return render(request, 'answer.html', dict(request.POST.items()))


def group_submissions(recs, name, group):
    data_frame = pd.DataFrame([[r.question_type, r.text_question, r.text_answer] for r in recs])
    data_frame.columns = ["TYPE", "QUESTION", "ANSWER"]
    for ((q, t), g) in data_frame.groupby(["QUESTION", "TYPE"]):
        gr = g.drop("TYPE",axis=1).groupby(["ANSWER"]).count()

        x = list(gr['QUESTION'].index)
        tot = gr['QUESTION'][x].sum()
        y = list(100 * gr['QUESTION'][x] / tot)
        p = list(gr['QUESTION'][x])
        
        group[q][name] = (x, y, p)



def form_report(request, app_id, offer_id, prof_id):
    appl = FormApplication.objects.get(id=app_id)
    offer = Offer.objects.get(id=offer_id)
    prof = Professor.objects.get(id=prof_id)

    recs = FormSubmission.objects.filter(form_application__id=app_id, offer__id=offer_id, professor__id=prof_id)
    recs_geral = FormSubmission.objects.filter(form_application__id=app_id)

    questions = defaultdict(dict)

    group_submissions(recs, 'CCR', questions)
    group_submissions(recs, 'Curso', questions)

    questions = [(k, [(c, x, y, p) for (c, (x, y, p)) in v.items()]) for (k,v) in questions.items()]

    return render(request, 'report.html', {'questions': questions})
