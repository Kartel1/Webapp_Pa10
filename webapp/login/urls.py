from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    # /login/
    url(r'^$', views.ConnexionView.as_view(), name='connexion'),

    url(r'modif/$',views.ModifUsager.as_view(), name='usager-modifier'),

    # /login/user_id
    url(r'^(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='detail'),
    #



]
