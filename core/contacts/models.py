from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField('Contacts full_name', max_length=70)
    email = models.EmailField('Contacts email')
    subject = models.CharField('Contacts subject', max_length=70)
    message = models.TextField('Contacts message')

    def __str__(self):
        return self.email
         
    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'