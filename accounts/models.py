from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from competitions.models import Lomba , Kategori

# Create your models here.
class Profile(models.Model):
    PARTI_LEVEL = (
        ("sd","SD"),
        ("smp","SMP"),
        ("sma","SMA"),
        ("univ","Universitas"),
        ("umum","Umum")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=True)
    
    participant_level = models.CharField(max_length=50,
       choices=PARTI_LEVEL,
       default='umum',)
    image = models.ImageField(default='default.jpg',blank=True, upload_to='profile_pics')
    favorite = models.ManyToManyField(Lomba)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)