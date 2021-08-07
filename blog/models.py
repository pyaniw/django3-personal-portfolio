from django.db import models

class all_blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images')

class all_blogs1(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images')

    def __str__(self):
        return self.title,self.description