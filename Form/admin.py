from django.contrib import admin

# Register your models here.
from Form.models import Lead

class LeadAdmin(admin.ModelAdmin):
    fields    = ('first_name', 'last_name', 'email','phone_number','modified')

    #list of fields to display in django admin
    list_display = ['last_name', 'first_name', 'email','phone_number','modified']


    #if you want django admin to show the search bar, just add this line
    search_fields = ['last_name', 'first_name']

    #to define model data list ordering
    ordering = ('id','last_name')





admin.site.register(Lead, LeadAdmin)
