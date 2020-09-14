from django.contrib import admin
from .models import PhrasesModel


@admin.register(PhrasesModel)
class PhrasesAdmin(admin.ModelAdmin):
    list_display = ('name', 'phrase', 'id', 'created_at')


