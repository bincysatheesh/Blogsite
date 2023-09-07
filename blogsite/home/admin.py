from django.contrib import admin
from . models import blogpost
from . models import latestpost
# from . models import login
# from . models import signup

# Register your models here.
admin.site.register(blogpost)
admin.site.register(latestpost)
# admin.site.register(login)
# admin.site.register(signup)

