from django.contrib import admin

# Register your models here.
from .models import Finch, Grubbing, Plaything

# Register your models here
admin.site.register(Finch)
admin.site.register(Grubbing)
admin.site.register(Plaything)
