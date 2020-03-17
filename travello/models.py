from django.db import models


#admin page user name-kaushal password-asusual

# Create your models here.
#For connecting databese
#make changes in setting.py
#include <webapp>.apps.<webapp>Config in INSTALLED_APPS
#command line python manage.py makemigrations
#migrartion file will be created
#in command line python manage.py sqlmigrate travello 0001
#python manage.py migrate 
#Table will be created in the database
class destination(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
