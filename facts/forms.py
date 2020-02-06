from django import forms


class Search(forms.Form):
    a = forms(max_length=100)

