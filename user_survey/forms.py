from django import forms
from django.core.exceptions import ValidationError
from college_display.models import Major

yes_no_choice = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]


class MajorSearch(forms.Form):
    major_query = forms.ModelMultipleChoiceField(queryset=Major.objects.all(), widget=forms.CheckboxSelectMultiple, label="")
    max_selections = 5

    def clean_major_query(self):
        data = self.cleaned_data['major_query']
        
        if len(data) > self.max_selections:
            raise ValidationError(f'You can select up to {self.max_selections} options only.')
        
        return data


class PriceSearch(forms.Form):
    price_ranges = [
        ('0 9999', 'Less than $10,000'),
        ('10000 29999', '$10,000 - $30,000'),
        ('30000 49999', '$30,000 - $50,000'),
        ('50000 69999', '$50,000 - $70,000'),
        ('70000 89999', '$70,000 - $90,000'),
        ('90000 10000000', 'More than $90,000')
    ]

    price_query = forms.ChoiceField(choices=price_ranges, label="")

class SportSearch(forms.Form):
    sport_query = forms.ChoiceField(choices=yes_no_choice, widget=forms.RadioSelect, label="")


class ArtsSearch(forms.Form):
    arts_query = forms.ChoiceField(choices=yes_no_choice, widget=forms.RadioSelect, label="")

class ProfessionalSearch(forms.Form):
    professional_query = forms.ChoiceField(choices=yes_no_choice, widget=forms.RadioSelect, label="")


class CityStateSearch(forms.Form):
    states = [
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
]
    city_query = forms.CharField(max_length=255, label="City")
    state_query = forms.ChoiceField(choices=states, label="State")


class InStateSearch(forms.Form):
    in_state_query = forms.ChoiceField(choices=yes_no_choice, widget=forms.RadioSelect, label="")


class PopulationSearch(forms.Form):
    pop_ranges = [
        ('0 999', 'Less than 1000 people'),
        ('1000 4999', '1000 - 5000 people'),
        ('5000 9999', '5000 - 10,000 people'),
        ('10000 24999', '10,000 - 25,000 people'),
        ('25000 10000000', 'More than 25,000 people')
    ]
    pop_query = forms.ChoiceField(choices=pop_ranges, label="")