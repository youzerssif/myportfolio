from django.db import models

# Create your models here.

class Portfolio(models.Model):
    """Model definition for Portfolio."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to="imageportfolio", null=True)
    lien = models.URLField(max_length=255, null=True)
    description = models.TextField(null=True)
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Portfolio."""

        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    # def __str__(self):
    #     """Unicode representation of Portfolio."""
    #     pass

