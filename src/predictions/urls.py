from django.urls import path
from .views import (
    PredictionList,
    PredictionDetailView,
    PredictionCreateView
)
app_name = 'predictions'
urlpatterns = [
    path('', PredictionList.as_view(), name='prediction_list'),
    path('<int:id>/', PredictionDetailView.as_view(), name='prediction_detail'),
    path('predict/', PredictionCreateView, name='prediction_create'),

]
