from django.contrib import admin

# Register your models here.

from .models import Content, Comment


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields' : ['title']}),
        ('Image', {'fields' : ['img']}), 
        ('Content', {'fields' : ['full_text']}),
        ('Date and Time', {'fields' : ['publication_date']}),
        ('Categories', {'fields' : ['status']}),
        ('Author', {'fields' : ['author']})
    
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



#admin.site.register(Content)



admin.site.register(Content, PostAdmin)
admin.site.register(Comment, CommentAdmin)