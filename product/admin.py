from django.contrib import admin

from .models import Product,Image, Category, Tag, ProductAttribute
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date', 'is_published', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category', 'content')
    list_filter = ('category', 'date', 'is_published', 'tags')
    readonly_fields = ('date', 'get_full_image')
    filter_horizontal = ('tags',)
    # inlines = (NewsAttributeStackedInline, AdditionalNewsInfoTabularInline)

    @admin.display(description='Изображение')
    def get_image(self, product: Product):
        return mark_safe(f'<img src="{product.image.first().image.url}" width="150px">')

    @admin.display(description='Изображение')
    def get_full_image(self, product: Product):
        return mark_safe(f'<img src="{product.image.url}" width="50%">')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ProductAttributeStackedInline(admin.StackedInline):
    model = ProductAttribute
    extra = 1


admin.site.register(Image)