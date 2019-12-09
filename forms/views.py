from django.shortcuts import render
from django.http import HttpResponse

from .models import FormTemplate

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
