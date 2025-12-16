from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioChangeForm, UsuarioCreationForm
from .models import Usuarios

# Register your models here.
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    list_display = ('correo', 'is_staff', 'is_superuser', 'is_active', 'activado_por',)
    list_filter = ('correo', 'is_staff', 'is_superuser', 'is_active', 'activado_por',)

    fieldsets = (
        (None, {'fields': ('correo', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'correo', 'password1', 'password2', 'is_staff', 'is_active',
                'groups', 'user_permissions'
            )}
        ),
    )

    search_fields = ('correo',)
    ordering = ('correo',)


admin.site.register(Usuarios, UsuarioAdmin)
