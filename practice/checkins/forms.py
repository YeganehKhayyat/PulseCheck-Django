from django import forms
from .models import MoodEntry


class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["score", "reason", "energy_level"]
        widgets = {
            'score' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder': '10' , 'rows':1 }),
            'reason' : forms.Textarea(attrs={'class' : 'form-control' ,'placeholder' : 'Enter here...'}),
            'energy_level' : forms.TextInput(attrs={'class' : 'form-control' ,'placeholder' : '8',}),
        }