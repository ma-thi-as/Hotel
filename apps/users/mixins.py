from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

class StaffOrAdminMixin:
    """ 
    Mixin para la validacion previa a hacer la solcitud http 
            Recive:
                    decorator para llamar a user passes test
                    recive una funcion o fun. lambda para obtener 
                    la unstancia del usuario y asi tener el staff o el superuser
                    y recibe como ultimo la url para el login
    """
    @method_decorator(user_passes_test(lambda user: user.is_staff | user.is_superuser, login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

