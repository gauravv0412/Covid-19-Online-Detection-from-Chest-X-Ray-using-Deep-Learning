from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import matplotlib.pyplot as plt
import cv2
import numpy as np
# from django.conf import settings 
from tensorflow.keras.models import *
import glob
import os

# Create your views here.
def predict(img_name):
    print('inside predict')
    img_path = '/app/'+ '/media/images/' + img_name
    # img_path = settings.BASE_DIR+ '/media/images/' + img_name
    img = cv2.imread(img_path)
    model_path = '/app/' + '/static/main/ml/model.h5'
    # model_path = settings.BASE_DIR + '/static/main/ml/model.h5'
    print('loading model')
    model = load_model(model_path)
    print('model loaded')
    img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
    img = img/255
    img = np.reshape(img, (1,224,224,3))
    print('predicting, on img:', img.shape)
    prob = model.predict(img)[0][0]
    prob = "{0:.2f}".format(prob) 
    prob = float(prob)
    if prob > 0.5 : 
        pred = 1
    else:
        pred = 0
    print(str(img_name), prob)
    print('going to return')  
    if pred == 1:
        return "Covid-19 Positive", prob
    else :
        return "Covid-19 Negative", prob

def index(request):
    print('inside index')
    error = None
    if request.method == 'POST': 
        form = XrayForm(request.POST, request.FILES) 
        print('POST request recieved.')
        if form.is_valid(): 
            print('saving img')
            with open('media/images/xray.jpg', 'wb+') as destination:
                for chunk in request.FILES['scan'].chunks():
                    destination.write(chunk)
            name = 'xray.jpg'
            print('saved:',name)
            # form.save() 
            print('calling predict')
            result, prob = predict(name)
            prob = float(prob)*100
            error = False
            return render(request, 'main/index.html', {'form':form, 'error':error, 'result':result, 'prob':prob, 'revprob':100 - prob})
        else:
            error = True
            message = "Unsupported Format"
            return render(request, 'main/index.html', {'form':form, 'error':error, 'message':message, 'result':None, 'prob':None})

    else:
        form = XrayForm()
    return render(request, 'main/index.html', {'form':form})
    # return HttpResponse('Hello, This is my Covid-19 Detector.')