from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Personne(models.Model):
    usager = models.ForeignKey(User, on_delete=models.CASCADE)
    user_infos = models.CharField(max_length=1000)
    user_logo = models.FileField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.usager)

    def get_absolute_url(self):
        return reverse('login:detail', kwargs={'slug': self.slug})



class Doc(models.Model):
    utilisateur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    fichier_titre = models.CharField(max_length=500)
    fichier_description = models.CharField(max_length=1000)
    fichier_file = models.FileField()
    is_favorite = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('login:detail', kwargs={'slug': self.utilisateur.slug})

    def __str__(self):
        return self.fichier_titre


