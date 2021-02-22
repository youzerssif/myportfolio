from django.db import models

# Create your models here.


class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    icon = models.FileField(upload_to="iconservice", null=True)
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
    
    
class Techno(models.Model):
    """Model definition for Techno."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Techno."""

        verbose_name = 'Techno'
        verbose_name_plural = 'Technos'

    def __str__(self):
        """Unicode representation of Techno."""
        return self.titre



class Skill(models.Model):
    """Model definition for Skill."""

    # TODO: Define fields here
    techno = models.ForeignKey(Techno, on_delete=models.CASCADE, related_name="skills")
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
        return self.techno

