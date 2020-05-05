from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from core import models as core_models
from django.utils import timezone
import csv

def increment(request):
    today = str(timezone.now().date())
    view, _  = core_models.Views.objects.get_or_create(date=today)
    view.counter = F('counter') + 1
    view.save(update_fields=["counter"])
    resp = HttpResponse("")
    resp['Content-Type'] = 'text/plain'
    return resp

def fetch(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="views.csv"'
    writer = csv.writer(response)
    for view in core_models.Views.objects.all():
        writer.writerow([view.date, view.counter])

    return response
