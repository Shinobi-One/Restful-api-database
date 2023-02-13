# pylint: disable=import-error
from django.contrib import admin
from app.models import Books,collection,Review,Customer
# Register your models here.
class show(admin.ModelAdmin):
    admin.site.register(Books,),
    admin.site.register(collection,)
    admin.site.register(Review,)
    admin.site.register(Customer,)