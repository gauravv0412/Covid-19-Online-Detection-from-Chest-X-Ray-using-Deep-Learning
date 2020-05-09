from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import matplotlib.pyplot as plt
import cv2
import numpy as np
from django.conf import settings 
from tensorflow.keras.models import *
import glob
import os

# Create your views here.
def predict(img_name):
    img_path = settings.BASE_DIR + '/media/images/' + str(img_name)
    img = cv2.imread(img_path)
    model_path = settings.BASE_DIR + '/static/main/ml/model.h5'
    model = load_model(model_path)
    img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
    img = img/255
    img = np.reshape(img, (1,224,224,3))
    prob = model.predict(img)[0][0]
    if prob > 0.5 : 
        pred = 1
    else:
        pred = 0
    
    print(str(img_name), prob)

    prob = "{0:.2f}".format(prob)
    if pred == 1:
        return "Positive"
    else :
        return "Negative"

def index(request):
    error = None
    if request.method == 'POST': 
        form = XrayForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            name = str(request.FILES['scan'])
            names = [x.split('/')[-1] for x in  glob.glob(settings.BASE_DIR + '/media/images/*')]
            if name in names or len(names) > 20:
                os.system('rm -rf ' + settings.BASE_DIR + '/media/images/')
            form.save() 
            result = predict(request.FILES['scan'])
            error = False
            return render(request, 'main/index.html', {'form':form, 'error':error, 'result':result})
        else:
            error = True
            message = "Unsupported Format"
            return render(request, 'main/index.html', {'form':form, 'error':error, 'message':message, 'result':None})

    else:
        form = XrayForm()
    return render(request, 'main/index.html', {'form':form})
    # return HttpResponse('Hello, This is my Covid-19 Detector.')