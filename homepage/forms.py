from django import forms
from .models import Report
from datetime import datetime 

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = [
            'street',
            'city',
            'state',
            'zipcode',
            'date',
        ]

        widgets = {
            'street': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'background-color: white',
            'placeholder': '123 Lane Street'}),

            'city': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'background-color: white',
            'placeholder': 'Los Angeles'}),

            'state': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'background-color: white',
            'placeholder': 'California'}),

            'zipcode': forms.NumberInput(attrs={
            'class': 'form-control',
            'style': 'background-color: white',
            'placeholder': '92699'}),

            'date': forms.DateInput(attrs={
            'class': 'form-control',
            'style': 'background-color: white',
            'placeholder': 'mm/dd/yyyy'}),
        }

    def clean_state(self, *args, **kwargs):
        state = self.cleaned_data.get('state')
        if state not in ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
                        "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
                        "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
                        "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
                        "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
                        "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                        "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
                        "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]:
        
            raise forms.ValidationError("Please enter a valid state")
        return state
    
    def clean_date(self, *args, **kwargs):
        date = str(self.cleaned_data.get('date'))

        date_object = datetime.strptime(date, "%Y-%m-%d")

        if date_object.year > 2020 or date_object.year <  2020:
            raise forms.ValidationError('Please enter "2020" as your year')
        return date

    def clean_street(self, *args, **kwargs):
        street = self.cleaned_data.get('street')
        
        check = ['!', '@', '#', '$', '%', '^','&','*','(', ')', '{', '}', '[', ']', '|', ';' ,':' ,'<', '>' , '?', '/' ,' " ' ,','] #except: periods apostrophe
        for i in check:
            if i in street:
                raise forms.ValidationError('Please enter a valid street')
        return street

    def clean_city(self, *args, **kwargs):
        city = self.cleaned_data.get('city')
        
        check = ['!', '@', '#', '$', '%', '^','&','*','(', ')', '{', '}', '[', ']', '|', ';' ,':' ,'<', '>' , '?', '/' ,' " ' , ','] #except: periods apostrophe
        for i in check:
            if i in city:
                raise forms.ValidationError('Please enter a valid city')
        return city
