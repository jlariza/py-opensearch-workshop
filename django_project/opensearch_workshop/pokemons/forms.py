from django import forms


class SearchPokemonForm(forms.Form):

    name = forms.CharField(required=False)
