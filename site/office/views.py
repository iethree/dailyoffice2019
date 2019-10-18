from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from office.offices import EveningPrayer


def evening_prayer(request, year, month, day):
    ep = EveningPrayer("{}-{}-{}".format(year, month, day))
    return render(request, "office/evening_prayer/ep.html", {"ep": ep})


def today_evening_prayer(request):
    return render(request, "office/evening_prayer/redirect.html", {})
