from django.contrib import admin
from .models import Image, User, Tier, SizedTier, SizedImage
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    add_fieldsets = (
        None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'tier')}),


admin.site.register(User, UserAdminConfig)
admin.site.register(SizedTier)
admin.site.register(SizedImage)
admin.site.register(Image)
admin.site.register(Tier)
