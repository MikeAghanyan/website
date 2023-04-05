from django.db import models
from django.urls import reverse

# Create your models here.        

# class CV(models.Model):
#     titel = models.CharField('CV titel', max_length=30)
#     cv = models.FileField('CV file', upload_to='media')

#     def __str__(self):
#         return self.titel

class HomeMotivation(models.Model):
    titel = models.CharField('HomeMotivation titel', max_length=30)
    icon = models.CharField('HomeMotivation icon', max_length=30)
    descr = models.CharField('HomeMotivation description', max_length=200)

    def __str__(self):
        return self.titel
    
class ProjectCategory(models.Model):
    name = models.CharField('ProjectCategory name', max_length=30)   
    descr = models.TextField('ProjectCaregory description', max_length=1500, blank=True)
    img_main = models.ImageField('ProjectCategory image', upload_to='media', blank=True)
    link = models.CharField('Article link', max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProjectCategory'
        verbose_name_plural = 'ProjectCategories'

class ServiceCategory(models.Model):
    name = models.CharField('ServiceCategory name', max_length=30)       
    descr = models.TextField('ServiceCaregory description', max_length=1500, blank=True)
    img_main = models.ImageField('ServiceCategory image', upload_to='media/Service_category', blank=True)
    link = models.CharField('Article link', max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ServiceCategory'
        verbose_name_plural = 'ServiceCategories'

class BlogCategory(models.Model):
    name = models.CharField('BlogCategory name', max_length=60)   
    active = models.BooleanField('Blog active', blank=True)
    descr = models.TextField('BlogCaregory description', max_length=1500, blank=True)
    img_main = models.ImageField('BlogCategory image', upload_to='media/Blog_category', blank=True)
    date = models.DateField('BlogCategory release time', blank=True)
    time = models.CharField('BlogCategory reading time', blank=True, max_length=2)
    link = models.CharField('Article link', max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogCategory'
        verbose_name_plural = 'BlogCategories'
        
class SubServiceCategory(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='service_categ')
    slug = models.SlugField('SubServiceCategory link', unique=True, blank=True)
    titel = models.CharField('SubServiceCategory titel', max_length=30)
    text1= models.TextField('SubServiceCategory text1', blank=True)
    text2= models.TextField('SubServiceCategory text2', blank=True)
    text3= models.TextField('SubServiceCategory text3', blank=True)
    text4= models.TextField('SubServiceCategory text4', blank=True)
    text5= models.TextField('SubServiceCategory text5', blank=True)
    text6= models.TextField('SubServiceCategory text6', blank=True)
    img_1 = models.ImageField('SubServiceCategory image1', upload_to='media/Service_category', blank=True)
    img_2= models.ImageField('SubServiceCategory image2', upload_to='media/Service_category', blank=True)
    img_3= models.ImageField('SubServiceCategory image3', upload_to='media/Service_category', blank=True)

    def __str__(self):
        return self.titel
    
    class Meta:
        verbose_name = 'SubServiceCategory'
        verbose_name_plural = 'SubServiceCategory'

class SubBlogCategory(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_categ')
    slug = models.SlugField('SubBlogCategory link', unique=True, blank=True)
    titel = models.CharField('SubBlogCategory titel', max_length=30)
    text1= models.TextField('SubBlogCategory text1', blank=True)
    text2= models.TextField('SubBlogCategory text2', blank=True)
    text3= models.TextField('SubBlogCategory text3', blank=True)
    text4= models.TextField('SubBlogCategory text4', blank=True)
    text5= models.TextField('SubBlogCategory text5', blank=True)
    text6= models.TextField('SubBlogCategory text6', blank=True)
    img_1 = models.ImageField('SubBlogCategory image1', upload_to='media/Blog_category', blank=True)
    img_2= models.ImageField('SubBlogCategory image2', upload_to='media/Blog_category', blank=True)
    img_3= models.ImageField('SubBlogCategory image3', upload_to='media/Blog_category', blank=True)
    
    def __str__(self):
        return self.titel
    
    class Meta:
        verbose_name = 'SubBlogCategory'
        verbose_name_plural = 'SubBlogCategories'