from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]
    
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'code',
        'name',
        'credit',
        'term',
        'year',
        'category'
        
        
    ]