from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# SAVE IT IF YOU WANT
# class pdf(models.Model):
#     person = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='pdf')
#     pdf = models.FileField(upload_to='pdfs/', null=True, validators=[FileExtensionValidator( ['pdf'])])
