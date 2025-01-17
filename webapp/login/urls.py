from django.conf.urls import url
from . import views


app_name = 'login'

urlpatterns = [
    # /login/
    url(r'^home/$', views.ConnexionView.as_view(), name='connexion'),

    # /login/register/
    url(r'register/$', views.UserFormView.as_view(), name='register'),

    # /login/modif/
    #url(r'modif/$',views.ModifUsager.as_view(), name='usager-modifier'),

    # /login/user/user_id/
    url(r'^user-(?P<slug>[\w-]+)/$', views.ProfileView.as_view(), name='detail'),

    # /login/user/user_id/
    url(r'^user-(?P<slug>[\w-]+)/update/$',views.ModifUpdate.as_view(), name='user-update'),

    url(r'^add_fichier/$',views.CreationFile.as_view(), name ='add_fichier'),

    url(r'logout/$',views.LogoutView.as_view(), name='logout'),

    url(r'^document/(?P<pk>[0-9]+)/delete/$',views.SuppressionFile.as_view(), name='file-delete'),
]
