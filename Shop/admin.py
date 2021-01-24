from django.contrib import admin

# Register your models here.
from Shop.models import Store


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','name','businessNum','status','category','date_joined','phone','address')
    list_filter = ('status','date_joined','category')
    search_fields = ['name']
    ordering = ('status','date_joined','name')
    fields = ('id','name','businessNum','status','facebook_url',"instagram_url","twitter_url","logo_img")
    filter_horizontal = ()
    readonly_fields = (
        'id',
        'date_joined',
        'phone',
        'address',        
        'ranking',
        'category',
        
    )



admin.site.register(Store,ShopAdmin)