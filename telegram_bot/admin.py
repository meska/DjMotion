from django.contrib import admin
from telegram_bot.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','username', 'first_name', 'last_name')
    #list_filter = ('server__name',)
    
admin.site.register(User,UserAdmin)
