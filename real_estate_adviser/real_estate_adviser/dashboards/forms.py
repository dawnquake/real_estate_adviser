from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Bar', max_length=100, widget=forms.TextInput())