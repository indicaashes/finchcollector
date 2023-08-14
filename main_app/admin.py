from django.contrib import admin

# Register your models here.
from .models import Finch, Grubbing

# Register your models here
admin.site.register(Finch)
admin.site.register(Grubbing)