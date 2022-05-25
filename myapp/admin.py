from pyexpat import model
from django.contrib import admin
from .models import Dog,Breed
# Register your models here.
@admin.register(Dog)
class dogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed','gender','color','favoritefood','favoritetoy',)
@admin.register(Breed)
class breedsAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'friendliness','trainability','sheddingamount','exerciseneeds',)
