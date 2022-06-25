from django.db import models

# Create your models here.
class HomeBG(models.Model):
    name1 = models.CharField('HomeBG name1', max_length=50)
    name2 = models.CharField('HomeBG name2', max_length=50)
    about = models.TextField('HomeBG about')
    price = models.IntegerField('HomeBG price', null=True, blank=True)
    img = models.ImageField('HomeBG image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeBG'
        verbose_name_plural = 'HomesBGs'

class TourIdea(models.Model):
    name = models.CharField('Tour name', max_length=30)
    about = models.TextField('Tour about')
    img = models.ImageField('Tour image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TourIdea'
        verbose_name_plural = 'TourIdeas'


class Comps(models.Model):
    name = models.CharField('Comps name', max_length=30)
    about = models.TextField('Comps about')
    img = models.ImageField('Comps image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comps'
        verbose_name_plural = 'Compses'