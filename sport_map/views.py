from django.shortcuts import render
import requests
import json


def index(request):
    return render(request, 'index.html', context={'spots': get_football_spots()})


def get_football_spots():
    url = 'https://maps.amsterdam.nl/_php/haal_objecten.php?TABEL=SPORT_OPENBAAR&SELECT=VOETBAL&SELECTIEKOLOM=SELECTIE&THEMA=sport&TAAL=en&BEHEER=0&NIEUW=niet&1587213497425'
    resp = requests.get(url)
    return json.loads(resp.text)