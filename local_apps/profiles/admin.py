from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ('name','duration',)
    list_display = ('name','duration',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
                'intra_user',
                'first_name',
                'last_name',
                'bio',
                'genre',
                'account',
                'avatar',
            )
    list_display = (
                    'intra_user',
                    'first_name',
                    'last_name',
                    'bio',
                    'genre',
                    'account',
                    'avatar',
                )
