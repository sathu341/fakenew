from django.shortcuts import redirect, render
from .models import User_tbl,Predict_tbl

# Create your views here.
def index(request):
    return render(request,'index.html')
def userreg(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        mobile=req.POST.get('mobile')
        obj=User_tbl.objects.filter(email=email,password=password)
        if obj:
            return render(req,'register.html',{'msg':"email and password already existings"}) 
        else:      

            obj=User_tbl.objects.create(name=name,email=email,password=password,mobile=mobile)
            if obj:
                obj.save()

                return render(req,'login.html',{'msg':"Successfully Register"})   
            else:
                return render(req,'register.html',{'msg':" Not Successfully Register"})   

    return render(req,'register.html')    
def login(req):
    if req.method=="POST":
        email=req.POST.get('email')
        password=req.POST.get('password')
        obj=User_tbl.objects.filter(email=email,password=password)
        if obj:
            req.session['email']=email
            req.session['password']=password
            for l in obj:
                userid=l.id
            req.session['userid']=userid    
            return render(req,'home.html',{'data':obj}) 

    return render(req,'login.html')       
def home(req):
    email=req.session['email']
    password=req.session['password']
    obj=User_tbl.objects.filter(email=email,password=password)
    if obj:
        return render(req,'home.html',{'data':obj})       
    else:
        return render(req,'index.html')    
    
def logout(req):
    req.session['email']=" "
    req.session['password']=" "

    return render(req,'index.html')       


def detection(request):
    if request.method=="POST":
        headline=request.POST.get("headline")
        userid=request.session['userid']
        
        result=processing(headline)
        result=result[0]
        obj=Predict_tbl.objects.create(userid=userid,headline=headline,result=result)
        obj.save()
        data=Predict_tbl.objects.filter(userid=userid)
        return render(request,'predict.html',{'result':result,'data':data})

def processing(headline):
    import pandas as pd
    import numpy as np
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import MultinomialNB
    import joblib
    dataset = pd.read_csv('fake_or_real_news.csv')

    dataset.drop(['Unnamed: 0'], axis=1, inplace=True)

    dataset.head()

    title = np.array(dataset["title"])
    label = np.array(dataset["label"])

    cv = CountVectorizer()
    title = cv.fit_transform(title)

    titletrain, titletest, labeltrain, labeltest = train_test_split(title, label, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(titletrain, labeltrain)
    joblib.dump(model,"fakemodel.sav")
   

    data = cv.transform([headline]).toarray()
    md=joblib.load("fakemodel.sav")
    
    print(md.predict(data))
    return md.predict(data)
            
def  headline(request):
    userid=request.session['userid']
    data=Predict_tbl.objects.filter(userid=userid)
    return render(request,'headline.html',{'data':data})     
def hdelete(req):
    idn=req.GET.get("hid")
    data=Predict_tbl.objects.get(id=idn)
    data.delete()
    return redirect("/headline")






    
