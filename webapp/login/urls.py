from django.conf.urls import url
from . import views


urlpatterns = [
    # /login/
    url(r'^$', views.connexion, name='connexion'),

    # /login/user_id
    url(r'^(?P<user_name_id>[0-9]+)/$', views.detail, name='detail')

]
