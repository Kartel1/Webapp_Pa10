from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from django.http import *
from django.conf import settings


from .models import Usager
from .forms import UserForm


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


class ModifUpdate(DeleteView):
    model=Usager
    fields = ['mail', 'password', 'user_name', 'user_logo']
    success_url =  reverse_lazy('login:connexion')

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
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('login:connexion')

class LogoutView(TemplateView):

  template_name = 'login/login_management.html'

  def get(self, request, **kwargs):

    logout(request)
    return render(request, self.template_name)







