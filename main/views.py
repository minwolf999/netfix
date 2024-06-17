from django.shortcuts import render
from django.contrib.auth import logout as django_logout

from services.models import Service, Request
from django.db.models import Count
from django.db.models import Prefetch



def home(request):
    request_service_ids = Request.objects.values_list('service_id', flat=True)
    services = Service.objects.prefetch_related(Prefetch('request_set', queryset=Request.objects.all())).filter(id__in=request_service_ids).annotate(request_count=Count('request'))
    services = services.order_by('-request_count')[:5]

    return render(request, "main/home.html", {'services': services})

def logout(request):
    django_logout(request)
    return render(request, "main/logout.html")
