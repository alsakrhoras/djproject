from django import forms
from.models import Lead


class AddLeadModelForm(forms.ModelForm):
    """
    making a form to create and add new leads to the database using model form in django
    """
    class Meta:
        """specifying the model"""
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )


class AddLeadForm(forms.Form):
    """
    making a form to create and add new leads to the database
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=18, max_value=180)
