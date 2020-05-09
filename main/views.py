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
    img_path = '/app/'+ '/media/images/' + str(img_name)
    img = cv2.imread(img_path)
    model_path = '/app/' + '/static/main/ml/model.h5'
    print('loading model')
    model = load_model(model_path)
    print('model loaded')
    img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
    img = img/255
    img = np.reshape(img, (1,224,224,3))
    print('predicting, on img:', img.shape)
    prob = model.predict(img)[0][0]
    if prob > 0.5 : 
        pred = 1
    else:
        pred = 0
    
    print(str(img_name), prob)
    prinnt('going to return')
    prob = "{0:.2f}".format(prob)   
    if pred == 1:
        return "Positive"
    else :
        return "Negative"

def index(request):
    print('inside index')
    error = None
    if request.method == 'POST': 
        form = XrayForm(request.POST, request.FILES) 
        print('POST request recieved.')
        print('Current Directory:')
        os.system('pwd')
        if form.is_valid(): 
            name = str(request.FILES['scan'])
            print(name)
            names = [x.split('/')[-1] for x in  glob.glob('/app/' + '/media/images/*')]
            print(names)
            if name in names or len(names) > 20:
                os.system('rm -rf ' + '/app/' + '/media/images/')
            print('saving form')
            form.save() 
            print('calling predict')
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