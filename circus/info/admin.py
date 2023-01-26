from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Obec, ObecAdmin, Kraj, KrajAdmin, Zastupitel, ZastupitelAdmin, ZastupitelKrajeAdmin, ZastupitelKraje

# Register your models here.
admin.site.register(Obec, ObecAdmin)
admin.site.register(Kraj, KrajAdmin)
admin.site.register(Zastupitel, ZastupitelAdmin)
admin.site.register(ZastupitelKraje, ZastupitelKrajeAdmin)

