from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_.models import Author


@admin.register(Author)
class MyUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_moderator')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )
    ordering = ('id',)
