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
    
class ServicesAll(models.Model):
    name = models.CharField('ServisesAll name', max_length=30)   
    slug = models.SlugField('ServicesAll link', unique=True, blank=True)
    img_main = models.ImageField('ServicessAll image', upload_to='media/service', blank=True)
    descr = models.CharField('ServicessAll description', max_length=300, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ServisesAll'
        verbose_name_plural = 'ServicesAll'

class Services(models.Model):
    titel = models.CharField('Services titel', max_length=30)
    text1= models.TextField('Services text1', blank=True)
    text2= models.TextField('Services text2', blank=True)
    text3= models.TextField('Services text3', blank=True)
    text4= models.TextField('Services text4', blank=True)
    text5= models.TextField('Services text5', blank=True)
    text6= models.TextField('Services text6', blank=True)
    img_1 = models.ImageField('Services image1', upload_to='media/service', blank=True)
    img_2= models.ImageField('Services image2', upload_to='media/service', blank=True)
    img_3= models.ImageField('Services image3', upload_to='media/service', blank=True)
    service_name = models.ForeignKey(ServicesAll, on_delete=models.CASCADE, related_name='services')


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
    active = models.BooleanField('Blog active')
    img1 = models.ImageField('Blog image', upload_to='media/blog', blank=True)
    img2 = models.ImageField('Blog image', upload_to='media/blog', blank=True)
    text1= models.TextField('Blog text1', blank=True)
    text2= models.TextField('Blog text2', blank=True)
    text3= models.TextField('Blog text3', blank=True)
    text4= models.TextField('Blog text4', blank=True)
    text5= models.TextField('Blog text5', blank=True)
    text6= models.TextField('Blog text6', blank=True)

    def __str__(self):
        return self.titel
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def get_absolute_url(self):
        return reverse("article_details", kwargs={"slug": self.slug})
    
class My(models.Model):
    img = models.ImageField('My img', upload_to='media/my')
    titel = models.CharField('Blog titel', max_length=30)
    descr = models.TextField('Blog description', max_length=1500)

    def __str__ (self):
        return self.titel
    
    class Meta:
        verbose_name = 'My'
        verbose_name_plural = 'My'



