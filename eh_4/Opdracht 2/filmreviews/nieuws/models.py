from django.db import models

class Nieuws(models.Model):
    koptekst = models.CharField(max_length=200)
    body = models.TextField()
    datum = models.DateField()

    def __str__(self):
        return self.koptekst
