from django.shortcuts import render

# Create your views here.

from django.http import Http404
from .models import Usager

def connexion(request):
    return render(request, 'login/connexion.html')

def detail(request, user_name_id):
    try:
        people = Usager.objects.get(pk=user_name_id)
        pic = people.user_logo
    except Usager.DoesNotExist:
        raise Http404("L'Utilisateur n'existe pas")

    return render(request, 'login/detail.html', {'utilisateur': people}, {'photo': pic})
