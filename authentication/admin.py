from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import *

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
  list_display = ('username', 'email', 'is_staff', 'activated')
  search_fields = ('username', 'email')
  fieldsets = (
    (None, {'fields': ('username', 'email', 'password', 'secret', 'activated',)}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'phone', 'password1', 'password2', "identity_type", 'identity_number'),
    }),
  )
  readonly_fields = ('id',)
  def save_model(self, request, obj, form, change):
    obj.username = obj.username.lower()
    obj.email = obj.email.lower()
    super().save_model(request, obj, form, change)
