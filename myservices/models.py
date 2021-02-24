from django.db import models

# Create your models here.


class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    # icon = models.FileField(upload_to="iconservice", null=True)
    description = models.TextField()
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.titre
    
    
class Metier(models.Model):
    """Model definition for Metier."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Metier."""

        verbose_name = 'Metier'
        verbose_name_plural = 'Metiers'

    def __str__(self):
        """Unicode representation of Metier."""
        return self.titre



class Skill(models.Model):
    """Model definition for Skill."""

    # TODO: Define fields here
    titre = models.CharField(max_length=250, null=True)
    metier = models.ManyToManyField(Metier, related_name="skills")
    pourcentage = models.IntegerField(null=True)
    icon = models.FileField(upload_to="iconskill", null=True)
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        return self.titre

