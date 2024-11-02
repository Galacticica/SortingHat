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
        ('<10000', 'Less than $10,000'),
        ('10000_30000', '$10,000 - $30,000'),
        ('30000_50000', '$30,000 - $50,000'),
        ('50000_70000', '$50,000 - $70,000'),
        ('70000_90000', '$70,000 - $90,000'),
        ('>90000', 'More than $90,000')
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
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]
    city_query = forms.CharField(max_length=255, label="City")
    state_query = forms.ChoiceField(choices=states, label="State")


class InStateSearch(forms.Form):
    in_state_query = forms.ChoiceField(choices=yes_no_choice, widget=forms.RadioSelect, label="")
