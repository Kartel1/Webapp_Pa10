from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.


class Personne(models.Model):
    usager = models.ForeignKey(User, on_delete = models.CASCADE)
    user_infos = models.CharField(max_length=1000)
    user_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('login:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return str(self.usager) + ' - ' + self.user_infos


