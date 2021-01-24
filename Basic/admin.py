from django.contrib import admin

# Register your models here.
from .models import Form



class FormAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','subject','status','date_created',)
    list_filter = ('status','date_created',)
    search_fields = ['name','subject']
    ordering = ('status','subject','name','date_created')
    fields = ('id','name','email','subject','status','message')
    filter_horizontal = ()
    readonly_fields = (
        'id',
        'message',        
        'name',
        'email',
        'subject',
        'date_created',
        
    )



admin.site.register(Form,FormAdmin)