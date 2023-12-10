from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)