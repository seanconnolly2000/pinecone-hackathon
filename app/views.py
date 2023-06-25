import os
from datetime import datetime
import json
import numpy as np
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import SignupForm
from .functions import function_manifest, openaif, set_biometric_vector, get_biometric_vector


# Home page index view - responsible for showing "cards" of information silos a user can use.
def home(request):
    items = [{'name': 'News & Weather', 'icon' : 'fa-sun-o', 'color' : 'bg-c-blue', 'description' : 'API calls for news and weather.  Also Time for datetime awareness.'},
             {'name': 'Employee Benefits', 'icon' : 'fa-university', 'color' : 'bg-c-yellow', 'description' : 'Employee Benefits accessible via Pinecone Full Text Search Vector Database'}
             ]
    if  request.user.is_authenticated:
        if request.user.groups.filter(name='Production').exists():
            items.insert(0,  {'name': 'Production', 'icon' : 'fa-cogs', 'color' : 'bg-c-indigo', 'description' : 'Production and manufacturing data stored in MS SQL.'})

        if request.user.groups.filter(name='Sales').exists():
            items.insert(0,  {'name': 'Sales', 'icon' : 'fa-shopping-cart', 'color' : 'bg-c-teal', 'description' : 'Sales data stored in MS SQL. '})

        if request.user.groups.filter(name='Purchasing').exists():
            items.insert(0,  {'name': 'Purchasing', 'icon' : 'fa-rocket', 'color' : 'bg-c-pink', 'description' : 'Purchasing data stored in MS SQL. '})

        if request.user.groups.filter(name='Human Resources').exists():
            items.insert(0,  {'name': 'Human Resources', 'icon' : 'fa-users', 'color' : 'bg-c-gray', 'description' : 'Human Resource data stored in MS SQL. '})
       
        # When a authenticated user enters the home page, reset the chat
        request.session['messages'] = []

    groups = []
    for g in request.user.groups.all():
        groups.append(g)

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'user':  request.user,
            'groups': groups,
            'session': request.session,
            'items' : items
        }
    )


# Biometric creation page
def biometric(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/biometric.html',
        {
            'title':'The Tiburon Sharks',
            'message':'Step up your security with biometric facial identity to protect your data.',
            'year':datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'The Tiburon Sharks',
            'message':'Helping you get to your corporate data quickly, safely, and securely.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About Us',
            'message':'The Tiburon Shaks was founded to bring you closer to your data.',
            'year':datetime.now().year,
        }
    )


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.set_password(form.cleaned_data['password1'])
            user.save()
            user = authenticate(username=username, password=form.cleaned_data['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
            return  HttpResponseRedirect('/')  
    else:
        form = SignupForm()
    return render(request, 'app/signup_form.html', {'form': form})


# Authenticate user setting biometric facial vector in Pinecone
@login_required
@api_view(['POST'])
def set_biometric_security(request):  
    data = request.data
    face_vector = data['face_vector']
    descriptor = face_vector['descriptor']
    score = face_vector['detection']['_score']
    vector = np.array(list(descriptor.values()), dtype=float).tolist()
    username = request.user.username
    if score > .95:
        set_biometric_vector(username, vector, score)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=406) # not acceptable
    

# Unauthenticated user trying to login with biometrics - no login required
@api_view(['POST'])
def get_biometric_security(request):  
    data = request.data
    face_vector = data['face_vector']
    descriptor = face_vector['descriptor']
    score = face_vector['detection']['_score']
    vector = np.array(list(descriptor.values()), dtype=float).tolist()

    # NEED TO TEST BOTH SCORE RETURNING AND THIS SCORE ABOVE
    username, score = get_biometric_vector(vector)
    if score > .95:
        user = User.objects.get(username=username)
         #manually set the backend attribute
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403) # forbidden
        

# Chatbot communication between the UI and OpenAI
@login_required
@api_view(['POST'])
def chat(request):  
   
    data = request.data
    question = data['message']

    # setup sys_context for usage in this function.  This is similar to what langchain does to "prime" ChatCompletion.
    # In this case, we want to provide useful information such as the person's name, and their email address - helpful for requests like "Email me the information"
    username = request.user.first_name + ' ' + request.user.last_name if request.user.first_name != '' else request.user.username
    sys_context = "The current user's name is " + username + ". The user's email is: " + request.user.email + ".  Only include data from function calls in your responses. If you don't know something, say 'I don't know.'"     
 
    messages = []
    # Get messages from session
    if 'messages' in request.session:
        messages = request.session['messages'] 

    if messages == []:
          messages = [{"role": "system", "content": sys_context}]

    f = function_manifest(request.user)
    openai_key = os.environ.get("OPENAI_APIKEY")
    oai = openaif(openai_key, f, messages)
    oai.temperature = 0
    
    res  = oai.user_request(question)

    # Refresh messages that were added via the chat interaction or function calls
    messages = oai.messages

     # We only have 4000 tokens, so the messages must be paired down regularly.  Remember to add the initial sys_context to element 0 
    if len(messages) > 10:
        messages = messages[-5:]
        messages.insert(0, {"role": "system", "content": sys_context})

    # Save the messages back to the session
    request.session['messages'] = messages

    # Replace the degree symbol
    response = res.replace('\u00b0F', ' degrees Fahrenheit').replace('\u00b0C',' degrees Celcius')
 
    data = json.dumps({'reply': response})
    return HttpResponse(data, content_type='application/json')

