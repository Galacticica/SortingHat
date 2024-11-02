from django import forms
from college_display.models import Major

class MajorSearch(forms.Form):
    major_query = forms.ModelMultipleChoiceField(queryset=Major.objects.all(), widget=forms.CheckboxSelectMultiple, label="")