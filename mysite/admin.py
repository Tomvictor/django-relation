from django.contrib import admin
from mysite.models import accounts
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Accountsinline(admin.StackedInline):
    model = accounts
    can_delete = False
    verbose_name_plural = 'accounts'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Accountsinline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)