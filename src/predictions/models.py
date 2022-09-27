from django.db import models
from django.urls import reverse

# Create your models here.


class Prediction(models.Model):
    r_and_d = models.DecimalField(
        max_digits=10000, decimal_places=4, null=False)
    administration = models.DecimalField(
        max_digits=10000, decimal_places=4, null=False)
    marketing_spend = models.DecimalField(
        max_digits=10000, decimal_places=4, null=False)
    predicted_value = models.DecimalField(
        max_digits=10000, decimal_places=4, default=0, null=False)

    def get_absolute_url(self):
        return reverse('predictions:prediction_detail', kwargs={'id': self.id})

    def list_redirect_url(self):
        return reverse('predictions:prediction_list')

    def predict_form_url(self):
        return reverse('predictions:prediction_create')

    def set_attr(self, vals):
        self.r_and_d = vals.get('r_and_d')
        self.administration = vals.get('administration')
        self.marketing_spend = vals.get('marketing_spend')
        self.predicted_value = vals.get('predicted_value')
        self.save()
