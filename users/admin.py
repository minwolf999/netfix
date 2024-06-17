from django.contrib import admin

from .models import User, Customer, Company


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'field')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('display_user', 'display_birth')

    def display_user(self, obj):
        return obj.user.username if obj.user else None

    def display_birth(self, obj):
        return obj.birth.strftime("%Y-%m-%d") if obj.birth else None

    display_user.short_description = 'User'
    display_birth.short_description = 'Birth'
