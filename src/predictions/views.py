

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView


from .models import Prediction
from .forms import PredictionForm
import pickle
import numpy as np
import pandas as pd
regmodel = pickle.load(open(
    'C:/Users/Kartik Yanigar/Desktop/Class/50Startups/src/predictions/regmodel.pkl', 'rb'))
scaler = pickle.load(open(
    'C:/Users/Kartik Yanigar/Desktop/Class/50Startups/src/predictions/scaling.pkl', 'rb'))


class PredictionList(ListView):
    template_name = 'predictions/prediction_list.html'
    queryset = Prediction.objects.all()


class PredictionDetailView(DetailView):
    template_name = 'predictions/prediction_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Prediction, id=id_)


def PredictionCreateView(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            vals = form.cleaned_data
            data = np.array(list(vals.values())).reshape(1, -1)
            new_data = scaler.transform(data)
            output = regmodel.predict(new_data)
            print(new_data)
            print(output)
            vals['predicted_value'] = output[0]

            obj = Prediction()
            obj.set_attr(vals)

            context = {
                'object': obj
            }
            return render(request, 'predictions/prediction_detail.html', context)
        else:
            print('Give Valid Data')
    else:
        form = PredictionForm()
        context = {
            'form': form
        }
        return render(request, 'predictions/prediction_create.html', context)
