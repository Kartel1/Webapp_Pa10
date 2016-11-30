from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Usager(models.Model):
    mail = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=250)
    user_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('login:connexion')
        #kwargs={'pk': self.pk}


    def __str__(self):
        return self.mail + ' - ' + self.user_name


