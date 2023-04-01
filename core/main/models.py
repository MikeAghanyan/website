from django.db import models
from django.urls import reverse

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
    
class Services(models.Model):
    titel = models.CharField('Services titel', max_length=30)
    img_main = models.ImageField('Services image', upload_to='media/service')
    descr = models.CharField('Services description', max_length=300)
    slug = models.SlugField('Services link', unique=True)
    text1= models.TextField('Services text1', blank=True)
    text2= models.TextField('Services text2', blank=True)
    text3= models.TextField('Services text3', blank=True)
    text4= models.TextField('Services text4', blank=True)
    text5= models.TextField('Services text5', blank=True)
    text6= models.TextField('Services text6', blank=True)
    img_1 = models.ImageField('Services image1', upload_to='media/service', blank=True)
    img_2= models.ImageField('Services image2', upload_to='media/service', blank=True)
    img_3= models.ImageField('Services image3', upload_to='media/service', blank=True)

    def __str__(self):
        return self.titel
    
    def get_absolute_url(self):
        return reverse("service_details", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

class Blog(models.Model):
    titel = models.CharField('Blog titel', max_length=60)
    img = models.ImageField('Blog image', upload_to='media/blog')
    descr = models.CharField('Blog description', max_length=300)
    date = models.DateField('Blog release time')
    time = models.CharField('Blog reading time', max_length=2)
    slug = models.SlugField('Blog link', unique=True)
    active = models.BooleanField('Blog active')


    def __str__(self):
        return self.titel
    
    def get_absolute_url(self):
        return reverse("article_details", kwargs={"slug": self.slug})
    
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

