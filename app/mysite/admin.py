from django.contrib import admin

from .models import Game, CategoryGame


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(CategoryGame)
class CategoryGameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

