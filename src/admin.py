from django.contrib import admin

# Register your models here.

from src.models import Interior_Designer
from src.models import Electrician
from src.models import Plumber
from src.models import Carpainter
from src.models import Painter
from src.models import Mechanic

admin.site.register(Interior_Designer) 
admin.site.register(Electrician) 
admin.site.register(Plumber) 
admin.site.register(Carpainter) 
admin.site.register(Painter) 
admin.site.register(Mechanic) 
