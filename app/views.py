from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Client


def client_orders(request, client_id):
    time_now = timezone.now()
    last_week = time_now - timedelta(days=7)
    last_month = time_now - timedelta(days=30)
    last_year = time_now - timedelta(days=365)
    client = Client.objects.get(id=client_id)

    context = {
        'client': client,
        'last_week': last_week.date(),
        'last_month': last_month.date(),
        'last_year': last_year.date(),
    }

    return render(request, 'client_orders.html', context)
