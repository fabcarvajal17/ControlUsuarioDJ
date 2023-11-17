from django import forms 
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'contraseña'
            }
        )

    )

    password2 = forms.CharField(
        label='contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'repetir contraseña'
            }
        )

    )


    class Meta:
        model = User
        fields = (
            'username',
            'nombres',
            'apellidos',
            'email',
            'genero',
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las Contraseñas NO coinciden')