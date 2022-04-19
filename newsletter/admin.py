from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from parler.admin import TranslatableAdmin
from newsletter.models import Category, Newsletter 
# Register your models here.

admin.site.register(Category, MPTTModelAdmin)

@admin.register(Newsletter)
class NewsletterAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {'fields': (
            'name',
            'category',
            'image', 
            'title', 
            'abstract', 
            'content',
            'active',
            )}
        ),
    )
    readonly_fields = ('date_created', 'date_updated',)
    list_filter = ('active','category','date_updated')
    list_display = ('id','name','category','active','date_created','date_updated')
    search_fields = ('name','title','category',)
    