from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UsuarioManager(BaseUserManager):
    """
        Clase para la personalización de usuarios donde el correo
        es el único identificador par la autenticación de un usuario
        en el aplicativo
    """
    def create_user(self, correo, password=None, **extra_fields):
        """
            Función para crear y guardar usuario ingresando el correo
            y la contraseña
        
            :param self: Objeto propio de la clase
            :param correo: Correo electrónico del usuario
            :param password: Contraseña del usuario
            :param extra_fields: Parámetros adicionales
        """
        if not correo:
            raise ValueError(_('El correo electrónico es obligatorio'))
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        """
            Función para la creación del superusuario
            
            :param self: Objeto propio de la clase
            :param correo: Correo electrónico del superusuario
            :param password: Contraseña del superusuario
            :param extra_fields: Parámetros adicionales
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('El superusuario de debe tener el campo is_staff=True.'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('El superusuario de debe tener el campo is_superuser=True.'))

        return self.create_user(correo, password, **extra_fields)