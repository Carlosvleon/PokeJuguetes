from django.forms import (
    Form,
    CharField,
    PasswordInput,
    BooleanField,
    CheckboxInput,
    TextInput,
    EmailInput
    # EmailField
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Formulario_login(Form):

    nombre_usuario = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese nombre de usuario',
        widget = TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Usuario'
            }
        )
    )
    contrasenia_usuario = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
    recuerdame = BooleanField(
        required = False,
        label = 'Recordarme',
        widget = CheckboxInput(
            
        )
    )

class Formulario_reg(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['password1'].widget.attrs = {'class' : 'form-control'}
        self.fields['password2'].widget.attrs = {'class' : 'form-control'}
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'

        ]
        widgets = {
            'username': TextInput( attrs={'class':'form-control'}),
            'first_name': TextInput( attrs={'class':'form-control'}),
            'last_name': TextInput( attrs={'class':'form-control'}),
            'email': EmailInput( attrs={'class':'form-control'}),


        }