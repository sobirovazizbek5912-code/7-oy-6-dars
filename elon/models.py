from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Qaysi kategoryaga tegishlilgi')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Bolim'
        verbose_name_plural='Bolimlar'
class Author(models.Model):

    MILD=[
        ('mild_a','millodan avvalgi'),
        ('mild','millodiy')
    ]

    full_name=models.CharField(max_length=255,verbose_name='Toliq ismi')
    address=models.CharField(max_length=150, null=True ,blank=True,verbose_name='Manzili')
    birth_year=models.PositiveIntegerField(verbose_name='Tugilgan yili')
    died_year=models.PositiveIntegerField(null=True,blank=True,help_text='Tirik bolsa yil kiritmang',verbose_name='Vafot etgan vaqti')
    mild=models.CharField(choices=MILD,default='mild',verbose_name='Qaysi davrda yashagani')


    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name='Muallif'
        verbose_name_plural='Mualliflar'
        ordering = ('-full_name',)

class Publisher(models.Model):
    name=models.CharField(max_length=150,unique=True,verbose_name='Nashriyot nomi')
    address=models.CharField(max_length=150,verbose_name='Manzili')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Nashriyot'
        verbose_name_plural='Nashriyot'


class Elon(models.Model):
    title = models.CharField(max_length=200,verbose_name='Nomi')
    price = models.IntegerField(verbose_name='narxi')
    description = models.TextField(verbose_name='Tarif')
    image = models.ImageField(upload_to='elons/',verbose_name='Rasmni yuklash')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ManyToManyField(Author,related_name='elons')
    publisher=models.ForeignKey(Publisher,on_delete=models.SET_NULL,null=True,verbose_name='Nashiryot')
    likes = models.ManyToManyField(User, related_name='liked_elons', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Elon'
        verbose_name_plural='Elonlar'


class Comment(models.Model):
    elon = models.ForeignKey(Elon, on_delete=models.CASCADE, related_name='comments',verbose_name='Elon')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,verbose_name='Foydalanuvchi')
    name = models.CharField(max_length=100,verbose_name='Nomi')
    text = models.TextField(verbose_name='Matn')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Bosib chiqarilgan vaqti')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Izoh'
        verbose_name_plural='Izohlar'