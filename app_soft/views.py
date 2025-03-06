from django.shortcuts import render


def about(request):
    return render(request, 'about.html')
def home(request):
    greeting = "Witaj na mojej stronie!"
    items = ["jabłko", "banan", "czereśnia"]


    # Kontekst, który przekazujemy do szablonu
    context = {
        'greeting': greeting,
        'items': items,
    }

    return render(request, 'index.html', context)

