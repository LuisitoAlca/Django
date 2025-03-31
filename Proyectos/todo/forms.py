from django import forms
forms .models import Tarea
class TareaForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields=["tarea"]