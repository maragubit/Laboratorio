from .models import Parametro
from django import forms

class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields= '__all__'


    def __init__(self, *args, **kwargs):
        super(ParametroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
