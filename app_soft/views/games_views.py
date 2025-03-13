from django.shortcuts import render
from app_soft.models import Games

def games_index(request):
    games = Games.objects.all().order_by('-id')

    # Kontekst, który przekazujemy do szablonu liste gier
    context = {
        'games': games,
    }

    return render(request, 'games_list.html', context)