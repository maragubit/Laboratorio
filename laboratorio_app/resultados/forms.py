from .models import Resultado
from django import forms

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields= '__all__'


    def __init__(self, *args, **kwargs):
        super(ResultadoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'