from django.contrib import admin

# Register your models here.
from .models import Article,Images


class ImagesInline(admin.StackedInline):
    model = Images

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','draft','pub_date','modified']
    list_editable = ['draft']
    prepopulated_fields={'slug':('title',)}
    inlines = [ImagesInline]

admin.site.register(Article,ArticleAdmin)
