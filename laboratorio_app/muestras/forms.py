from .models import Muestra

from django import forms
import datetime
from datetime import datetime
from django.forms.widgets import CheckboxSelectMultiple,SelectDateWidget

now=datetime.now().year
class MuestraForm(forms.ModelForm):
    class Meta:
        model = Muestra
        exclude = ['muestreo','idinicial','idfinal']
        widgets = {

            'parametros': forms.CheckboxSelectMultiple,
            'fecha': SelectDateWidget(years=range(now- 5, now+1)),
        }



    def __init__(self, *args, **kwargs):
        super(MuestraForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'parametros':
                if field.widget.attrs.get('class'):
                    field.widget.attrs['class'] += ' form-control'
                else:
                    field.widget.attrs['class']='form-control'

