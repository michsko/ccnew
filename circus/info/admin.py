from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Obec, ObecAdmin 
from .models import Kraj, KrajAdmin
from .models import Zastupitel, ZastupitelAdmin
from .models import ZastupitelKrajeAdmin, ZastupitelKraje
from .models import VolebVyslPrez2023Obec2kolo, VolebVyslPrez2023Obec2koloAdmin
from .models import VolebVyslPrez2023Obec1kolo, VolebVyslPrez2023Obec1koloAdmin
# Register your models here.
admin.site.register(Obec, ObecAdmin)
admin.site.register(Kraj, KrajAdmin)
admin.site.register(Zastupitel, ZastupitelAdmin)
admin.site.register(ZastupitelKraje, ZastupitelKrajeAdmin)
admin.site.register(VolebVyslPrez2023Obec1kolo,VolebVyslPrez2023Obec1koloAdmin)
admin.site.register(VolebVyslPrez2023Obec2kolo,VolebVyslPrez2023Obec2koloAdmin)

