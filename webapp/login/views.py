from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin,FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User
from django.http import *
from django.conf import settings



from .models import Personne,Doc
from .forms import UserForm



class ConnexionView(generic.ListView):
    template_name = 'login/connexion.html'

    def get_queryset(self):
        return Personne.objects.all()

class ProfileView(generic.DetailView):
    model = Personne
    template_name = 'login/detail.html'


class ModifUsager(CreateView):
    model = Personne
    fields = ['user_infos', 'user_logo']


class CreationFile(CreateView):
    model = Doc
    fields = ['fichier_titre', 'fichier_description', 'fichier_file']
    def form_valid(self, form):
        form.instance.utilisateur = self.request.user.personne_set.get()
        return super(CreationFile, self).form_valid(form)

class ModifUpdate(UpdateView):
    model = Personne
    fields = ['user_infos', 'user_logo']
    #success_url =  reverse_lazy('login:details')

class UserFormView(View):
    form_class = UserForm
    template_name = 'login/registration_form.html'

    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form' : form})

    #process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user.personne_set.create(user_logo = 'Anonymous.png', slug = username )

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('login:connexion')

        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):

    template_name = 'login/login_management.html'
    def post(self, request, **kwargs):
        global id
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        user = authenticate(username=username, password=password)
        id = user.pk
        if user is not None and user.is_active:
            login(request, user)
            return redirect('login:connexion')

class LogoutView(TemplateView):

  template_name = 'login/login_management.html'

  def get(self, request, **kwargs):

    logout(request)
    return render(request, self.template_name)







