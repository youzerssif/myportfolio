from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'titre', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('titre')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Service')
    active.short_description = 'active Service'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Service')
    desactive.short_description = 'desactive Service'
    ordering = ('titre',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('view_image', 'titre',)

    def view_image(self, obj):
        try:
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.icon.url))
        except Exception as e:
            print(e)
    

@admin.register(models.Techno)
class TechnoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('titre')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Techno')
    active.short_description = 'active Techno'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Techno')
    desactive.short_description = 'desactive Techno'
    ordering = ('titre',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('titre',)

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'techno', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('techno')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Skill')
    active.short_description = 'active Skill'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Skill')
    desactive.short_description = 'desactive Skill'
    ordering = ('techno',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('view_image', 'techno',)

    def view_image(self, obj):
        try:
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.icon.url))
        except Exception as e:
            print(e)