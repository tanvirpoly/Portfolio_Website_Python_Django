
from django.contrib import admin

from portfolio.models import About, Email, Global, Phone, Social,Address,Skills

# Register your models here.
admin.site.register(Social)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Global)
admin.site.register(Skills)
admin.site.register(About)