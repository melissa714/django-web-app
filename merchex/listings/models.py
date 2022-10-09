from email.policy import default
from secrets import choice
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP ='HH'
        SYHTH_POP ='SP'
        ALTERNATIVE_ROCK ='AR'
        
    name = models.CharField(max_length=100)
    genre=models.CharField(max_length=100,choices=Genre.choices)
    biography=models.CharField(max_length=255)
    year_formed=models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active=models.BooleanField(default=True)
    official_homepage=models.URLField(null=True,blank=True)
    #like_new =models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return f'{self.name}'

class Listing(models.Model):
    class Annonce(models.TextChoices):
        RECORDS='RD'
        CLOTHING='CL'
        POSTERS='PO'
        MISCELLANEAOUS='MS'
    Title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    sold = models.BooleanField(default=True)
    year = models.DateField(null=True)
    type=models.CharField(max_length=100,choices=Annonce.choices)
    band=models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.Title}'