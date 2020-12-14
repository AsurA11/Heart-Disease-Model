from django.shortcuts import render,HttpResponse
import joblib
import numpy as np
import pandas as pd


mo= joblib.load("heartdisease.pkl")

# Create your views here.
def index(request):
    
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        lis=[]

        age=request.POST.get('Age')
        lis.append(age)

        sex=request.POST.get("Sex")
        if(sex=="Male"):
            sex=1
            lis.append(sex)
        else:
            sex=0
            lis.append(sex)
        

        cp=request.POST.get("Chest Pain Type")
        if(cp=="typical angina"):
            cp=0
            lis.append(cp)
        elif(cp=="atypical angina"):
            cp=1
            lis.append(cp)
        elif(cp=="non-anginal pain"):
            cp=2
            lis.append(cp)
        else:
            cp=3
            lis.append(cp)

        trestbps=request.POST.get("Blood Pressure")
        lis.append(trestbps)

        chol=request.POST.get("Serum Cholestoral")
        lis.append(chol)

        fbs=request.POST.get("Fasting Blood Sugar > 120 mg/dl")
        if(fbs=="True"):
            fbs=1
            lis.append(fbs)
        else:
            fbs=0
            lis.append(fbs)

        restecg=request.POST.get("Resting Electrocardiographic Measurement")    
        if(restecg=="normal"):
            restecg=0
            lis.append(restecg)
        elif(restecg=="ST-T wave abnormality"):
            restecg=1
            lis.append(restecg)
        else:
            restecg=2
            lis.append(restecg)

        thalach=request.POST.get("Heart Rate")
        lis.append(thalach)

        exang=request.POST.get("Exercise Induced Angina")
        if(exang=="Yes"):
            exang=1
            lis.append(exang)
        else:
            exang=0
            lis.append(exang)

        oldpeak=request.POST.get("ST Depression")
        lis.append(oldpeak)

        slope=request.POST.get("Slope of the peak exercise ST segment")
        if(slope == "upsloping"):
            slope=0
            lis.append(slope)
        elif(slope == "flat"):
            slope=1
            lis.append(slope)
        else:
            slope=2
            lis.append(slope)

        ca=request.POST.get("Number of major vessels")
        lis.append(ca)

        thal=request.POST.get("Thalassemia")
        if(thal == "normal"):
            thal=0
            lis.append(thal)
        elif(thal == "fixed defect"):
            thal=1
            lis.append(thal)
        elif(thal == "reversable defect"):
            thal=2
            lis.append(thal)
        else:
            thal=3
            lis.append(thal)

    features_value = [np.array(lis)]

    features_name = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']

    df = pd.DataFrame(features_value, columns=features_name)
    output = mo.predict(df)[0] 
    if(output == 1):
        val="Patient has Heart Disease"
    else:
        val="Patient has no  Heart Disease"

    context={"val":val}
    
    return render(request, 'result.html' ,context)
         