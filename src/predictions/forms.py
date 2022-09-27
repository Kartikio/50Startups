# from django.forms import forms
from django import forms
from .models import Prediction


class PredictionForm(forms.ModelForm):
    r_and_d = forms.DecimalField(
        max_digits=10000, decimal_places=4)
    administration = forms.DecimalField(
        max_digits=10000, decimal_places=4)
    marketing_spend = forms.DecimalField(
        max_digits=10000, decimal_places=4)

    class Meta:
        model = Prediction
        fields = [
            'r_and_d',
            'administration',
            'marketing_spend'
        ]

    # def give_attr(self):
    #     res = {
    #         'r_and_d': self.r_and_d,
    #         'administration': self.administration,
    #         'marketing_spend': self.marketing_spend
    #     }
    #     return res
