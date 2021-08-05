from django.contrib import admin

# Register your models here.

from .models import Content


class ContentAdmin(admin.ModelAdmin):
    fieldsets = [('Content', {'fields' : ['title', 'full_text']}), 
    ('Image', {'fields' : ['img']}), ('Date and Time', {'fields' : ['publication_date']})]

admin.site.register(Content)

#admin.site.register(Content, ContentAdmin)