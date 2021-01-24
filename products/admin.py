from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',
                    'store', 'active', 'quantity', 'description')
    list_filter = ('category', 'title', 'store')
    search_fields = ['title']
    ordering = ('category', 'title', 'store')
    fields = ('id', 'title', 'price', 'category', 'store',
              'active', 'quantity', 'description', 'img')
    filter_horizontal = ()
    readonly_fields = (
        'id',
        'active',

    )


admin.site.register(Product, ProductAdmin)
