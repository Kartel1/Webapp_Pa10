from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import Http404
from .models import Usager

def connexion(request):
    return render(request, 'login/connexion.html')

def detail(request, user_name_id):
    people = get_object_or_404(Usager,pk=user_name_id)
    return render(request, 'login/detail.html', {'utilisateur': people})
