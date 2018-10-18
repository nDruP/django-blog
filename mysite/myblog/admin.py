from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-N/A-'
    inlines = [
        CategoryInline,
    ]
    #if you use customize admin panel and add filter then uncomment  following line
    '''
    list_filter=('title','published_date')
    search_fields=('title','author')
     '''


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-N/A-'
    exclude = ('posts',)
    #if you use customize admin panel and add filter then uncomment  following line
    '''
    list_filter=('name','published_date')
    search_fields=('name','description')
     '''