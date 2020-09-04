from django.contrib import admin

# Register your models here.
from .models import Lomba, Kategori
admin.site.register(Lomba)
admin.site.register(Kategori)

