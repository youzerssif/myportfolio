from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    image = CloudinaryField('imageblog')
    description = models.TextField()
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-date_add']

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre