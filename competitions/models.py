from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from taggit_autosuggest.managers import TaggableManager
from datetime import date,datetime
# Create your models here.

class Lomba(models.Model):
    #Contains all the lomba

    COMP_LEVEL = (
        ("lokal","Lokal"),
        ("nasional","Nasional"),
        ("internasional","Internasional")
    )

    PARTI_LEVEL = (
        ("sd","SD"),
        ("smp","SMP"),
        ("sma","SMA"),
        ("univ","Universitas"),
        ("umum","Umum")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey('Kategori', on_delete=models.SET_NULL, null=True)
    jumlahhadiah = models.DecimalField(max_digits=9 , decimal_places=2)

    created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    tanggalpelaksanaan = models.DateTimeField()
    
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    owner_email = models.EmailField(null=True)
    visited = models.IntegerField(default=0)
    link = models.URLField(null=True)
    tags = TaggableManager(blank=True)    

    competitions_level = models.CharField(max_length=50,
       choices=COMP_LEVEL,
       default='nasional',)
    participant_level = models.CharField(max_length=50,
       choices=PARTI_LEVEL,
       default='umum',)

    active = models.BooleanField(default=True)


    image = models.ImageField(upload_to='poster/' , blank=True , null=True)

    slug = models.SlugField(blank=True , null=True)

    def save(self, *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Lomba , self).save(*args , **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('competitions:detail_lomba', kwargs={'pk': self.pk , 'slug': self.slug})

    @property
    def days_remaining(self):
        today = datetime.today()
        result = self.deadline - today
        if result.days > 0 :
            return result.days
        else:
            return abs(result.days)
            


class Kategori(models.Model):
    #Contains all category

    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kategori/' , blank=True , null=True)
    slug = models.SlugField(blank=True , null=True)
    def save(self, *args , **kwargs):
        if not self.slug and self.category_name :
            self.slug = slugify(self.category_name)
        super(Kategori , self).save(*args , **kwargs)

    def __str__(self):
        return self.category_name

