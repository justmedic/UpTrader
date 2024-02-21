from django.contrib import admin
from .models import MenuItem, MenuDisplayPage

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    search_fields = ('name',)
    
    class MenuDisplayPageInline(admin.TabularInline):
        model = MenuItem.display_on_pages.through
        extra = 1

    inlines = [MenuDisplayPageInline]

@admin.register(MenuDisplayPage)
class MenuDisplayPageAdmin(admin.ModelAdmin):
    list_display = ('url',)
