from django.db import models
# Create your models here.

class blogpost(models.Model):
    pic=models.ImageField(upload_to='images')
    dat= models.DateField()
    mt=models.CharField(max_length=50)
    st=models.CharField(max_length=80)
    descriptions=models.TextField(default='nothing')
    authorname=models.CharField(max_length=50)
class latestpost(models.Model):
    pic=models.ImageField(upload_to='images1')
    dat= models.DateField()
    mt=models.CharField(max_length=50)
    st=models.CharField(max_length=80)
# class login(models.Model):
#     un=models.CharField(max_length=60)
#     un=models.CharField(max_length=25)
# class signup(models.Model):
#     fn=models.CharField(max_length=60)
#     ln=models.CharField(max_length=25)
#     email=models.EmailField(max_length=100)
#     usn=models.CharField(max_length=60)
#     pwd=models.CharField(max_length=25)
#     cp=models.CharField(max_length=25)


    