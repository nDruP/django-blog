from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-N/A-'
    inlines = [
        CategoryInline,
    ]
    
admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-N/A-'
    exclude = ('posts',)
admin.site.register(Category, CategoryAdmin)
