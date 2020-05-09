from django import forms
from .models import *

class XrayForm(forms.ModelForm):

    class Meta:
        model = Xray
        fields = ['scan']