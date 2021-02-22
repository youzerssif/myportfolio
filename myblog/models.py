from django.db import models

# Create your models here.


class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    titre = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to="imageblog", null=True)
    description = models.TextField()
    
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre