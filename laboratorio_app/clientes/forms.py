from .models import Cliente
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['proxima_visita']


    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
