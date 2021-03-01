from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(models.Apropos)
class AproposAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'nom', 'email', 'numero', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('nom')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Apropos')
    active.short_description = 'active Apropos'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Apropos')
    desactive.short_description = 'desactive Apropos'
    # ordering = ('nom',)
    # list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('view_image', 'nom',)

    def view_image(self, obj):
        try:
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
        except Exception as e:
            print(e)
    

@admin.register(models.Statistique)
class StatistiqueAdmin(admin.ModelAdmin):
    list_display = ('client_heureux','projet_realises','heures_works', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('client_heureux','projet_realises','heures_works')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Statistique')
    active.short_description = 'active Statistique'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Statistique')
    desactive.short_description = 'desactive Statistique'
    # ordering = ('client_heureux','projet_realises','heures_works')
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('client_heureux',)


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('nom','email', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('nom','email',)
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Newsletter')
    active.short_description = 'active Newsletter'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Newsletter')
    desactive.short_description = 'desactive Newsletter'
    ordering = ('nom','email',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('nom',)
    
    
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','email','numero', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('nom','email','numero')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Contact')
    active.short_description = 'active Contact'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Contact')
    desactive.short_description = 'desactive Contact'
    ordering = ('nom','email','numero')
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('nom',)