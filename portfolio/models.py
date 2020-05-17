from django.db import models


# Create your models here.


class PortfolioModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    # Blank is used to make this URL field optional

    def __str__(self):
        return self.title


class PicsHappie(models.Model):

    pictitle = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='portfolio/images/')
    picdate = models.DateField()

    def __str__(self):
        return self.pictitle
