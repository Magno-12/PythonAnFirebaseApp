import re
from urllib import response
from django.shortcuts import render
import pyrebase
from django.contrib import auth
import requests
import json

config={
    'apiKey' : "AIzaSyD_6AVv3DvM6KfrKBnQJgqdyiR4otSDuQ0",
    'authDomain' : "logindjangoprueba.firebaseapp.com",
    'projectId' : "logindjangoprueba",
    'storageBucket' : "logindjangoprueba.appspot.com",
    'messagingSenderId' : "791591105335",
    'appId' : "1:791591105335:web:b71a9d2e8121b7717e20b2",
    'measurementId' : "G-HKL2L0NL1S",
    'databaseURL' : "https://logindjangoprueba-default-rtdb.firebaseio.com"
}
firebase = pyrebase.initialize_app(config)
auth2 = firebase.auth()
database=firebase.database()
url = "https://api.chucknorris.io/jokes/random"

def signIn(request):
    return render(request,"Login.html")

def button(request):
    response = requests.get(url)
    jokes = response.json()["value"]
    print(jokes)
    return render(request, "jokes.html",{'jokes':jokes})

def buttonFav(request):
    query = request.GET.get("phrase")
    database.child('phrase').push({'phrase':query})
    return render(request, "jokes.html")

def listOfJokes():
    pass

def postsignIn(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = auth2.sign_in_with_email_and_password(email,passw)
    except:
        print(user)
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"jokes.html")