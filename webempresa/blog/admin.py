from django.contrib import admin
from .models import category,post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields =('created','update')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created','update')
    list_display =('title','author','published','post_categories')
    ordering =('author','published')
    search_fields =('title','author__username','cotegories__name')
    date_hierarchy ='published'
    list_filter =('author__username','cotegories__name')

    def post_categories (self,obj):
        return ",".join([c.name for c in obj.cotegories.all().order_by("name")])
    post_categories.short_description="Categorias"

admin.site.register(category,CategoryAdmin)
admin.site.register(post,PostAdmin)