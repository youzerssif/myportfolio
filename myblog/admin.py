from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('view_image', 'titre', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_field = ('titre')
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer une Article')
    active.short_description = 'active Article'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver une Article')
    desactive.short_description = 'desactive Article'
    ordering = ('titre',)
    list_per_page = 100
    date_hierarchy = ('date_add')
    list_display_links = ('view_image', 'titre',)

    def view_image(self, obj):
        try:
            return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
        except Exception as e:
            print(e)
    