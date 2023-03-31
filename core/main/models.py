from django.db import models

# Create your models here.        
class HomeMotivation(models.Model):
    titel = models.CharField('HomeMotivation titel', max_length=30)
    icon = models.CharField('HomeMotivation icon', max_length=30)
    descr = models.CharField('HomeMotivation description', max_length=200)

    def __str__(self):
        return self.titel

class Project(models.Model):
    titel = models.CharField('Project titel', max_length=30)
    img = models.ImageField('Project image', upload_to='media/porfolio')
    descr = models.CharField('Project description', max_length=55)
    slug = models.SlugField('Project link', unique=True, blank=True)
    active = models.BooleanField('Project active')


    def __str__(self):
        return self.titel
    
class Service(models.Model):
    titel = models.CharField('Service titel', max_length=30)
    img = models.ImageField('Service image', upload_to='media/service')
    descr = models.CharField('Service description', max_length=300)
    slug = models.SlugField('Service link', unique=True)

    def __str__(self):
        return self.titel
    
class Blog(models.Model):
    titel = models.CharField('Blog titel', max_length=30)
    img = models.ImageField('Blog image', upload_to='media/blog')
    descr = models.CharField('Blog description', max_length=300)
    date = models.DateField('Blog release time')
    time = models.CharField('Blog reading time', max_length=2)
    slug = models.SlugField('Blog link', unique=True)
    active = models.BooleanField('Blog active')


    def __str__(self):
        return self.titel
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

class My(models.Model):
    img = models.ImageField('My img', upload_to='media/my')
    titel = models.CharField('Blog titel', max_length=30)
    descr = models.TextField('Blog description', max_length=1500)

    def __str__ (self):
        return self.titel
    
    class Meta:
        verbose_name = 'My'
        verbose_name_plural = 'My'
