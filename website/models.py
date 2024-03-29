from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Apropos(models.Model):
    """Model definition for Apropos."""

    # TODO: Define fields here
    nom = models.CharField(max_length=200, null=True)
    image = CloudinaryField('monimage')
    description = models.TextField()
    email = models.EmailField(max_length=254, null=True)
    numero = models.CharField(max_length=50, null=True)
    lieu = models.CharField(max_length=50, null=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    googlemap = models.CharField(max_length=254, null=True)
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Apropos."""

        verbose_name = 'Apropos'
        verbose_name_plural = 'Aproposs'

    def __str__(self):
        """Unicode representation of Apropos."""
        return self.nom


class Statistique(models.Model):
    """Model definition for Statistique."""

    # TODO: Define fields here
    client_heureux = models.IntegerField()
    projet_realises = models.IntegerField()
    heures_works = models.IntegerField()
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Statistique."""

        verbose_name = 'Statistique'
        verbose_name_plural = 'Statistiques'

    # def __str__(self):
    #     """Unicode representation of Statistique."""
    #     pass


class Newsletter(models.Model):
    """Model definition for Newsletter."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Newsletter."""

        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        """Unicode representation of Newsletter."""
        return self.nom


class Contact(models.Model):
    """Model definition for Contact."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=50, null=True)
    sujet = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    message = models.TextField()
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.sujet
