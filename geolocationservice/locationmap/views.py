from django.shortcuts import render
from .models import Locationmap
from django.conf import settings
from django.contrib.auth.decorators import login_required
from companies.models import Company


@login_required
def map(request):
    company = Company.objects.get(user=request.user)

    context = {
        'location': Locationmap.objects.filter(company=company).all(),
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'locationmap/map.html', context)
