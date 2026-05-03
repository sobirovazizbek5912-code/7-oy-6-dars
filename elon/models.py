from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Author(models.Model):

    MILD=[
        ('mild_a','millodan avvalgi'),
        ('mild','millodiy')
    ]

    full_name=models.CharField(max_length=255)
    address=models.CharField(max_length=150, null=True ,blank=True)
    birth_year=models.PositiveIntegerField()
    died_year=models.PositiveIntegerField(null=True,blank=True,help_text='Tirik bolsa yil kiritmang')
    mild=models.CharField(choices=MILD,default='mild')


    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name=models.CharField(max_length=150,unique=True)
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Elon(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='elons/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ManyToManyField(Author,related_name='elons')
    publisher=models.ForeignKey(Publisher,on_delete=models.SET_NULL,null=True)
    likes = models.ManyToManyField(User, related_name='liked_elons', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    elon = models.ForeignKey(Elon, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name