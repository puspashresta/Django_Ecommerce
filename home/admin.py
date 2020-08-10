from django.contrib import admin

# Register your models here.
from home.models import *

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Item)
admin.site.register(Banner)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Cart)
