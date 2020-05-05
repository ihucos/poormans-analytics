from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from core import models as core_models
from django.utils import timezone

def increment(request):
    today = str(timezone.now().date())
    view = core_models.Views.objects.get_or_create(date=today)
    #view.count = F('count') + 1
    #view.save(update_fields=["count"])
