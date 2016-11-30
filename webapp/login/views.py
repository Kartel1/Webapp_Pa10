from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Usager


class ConnexionView(generic.ListView):
    template_name = 'login/connexion.html'

    def get_queryset(self):
        return Usager.objects.all()

class ProfileView(generic.DetailView):
    model = Usager
    template_name = 'login/detail.html'

class ModifUsager(CreateView):
    model=Usager
    fields = ['mail', 'password', 'user_name', 'user_logo']

class ModifUpdate(UpdateView):
    model=Usager
    fields = ['mail', 'password', 'user_name', 'user_logo']