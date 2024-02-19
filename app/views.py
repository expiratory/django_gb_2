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
        'time_range': [
            [7, last_week.date()],
            [30, last_month.date()],
            [365, last_year.date()],
        ],
    }

    return render(request, 'client_orders.html', context)
