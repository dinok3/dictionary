from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse_lazy
import requests
import json
from django.conf import settings



# Create your views here.


def home(request):

    if request.method == "GET":
        if request.GET:
            word = request.GET["word"]
          
            return redirect(reverse_lazy("search",args=[word]))
    return render(request,"main/home.html")


#raise and error || return json response
def catch_invalid_word_error(response):
    try:
        results = response.json()
        return response.json()
    except:
        
        raise Http404("Invalid word!")




def search(request,word):
    URL = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + settings.LANGUAGE + "/" + word.lower()
    response = requests.get(URL,headers={"app_id":settings.API_ID,"app_key":settings.API_KEY})
    
    json_response = catch_invalid_word_error(response)
    
    if len(json_response) == 1:
        raise Http404("Word not found in dictionary")

    return render(request,"main/search.html",{"response":json_response})



def json_response(request,word):
    URL = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + settings.LANGUAGE + "/" + word.lower()
    response = requests.get(URL,headers={"app_id":settings.API_ID,"app_key":settings.API_KEY})

    return JsonResponse(response.json(),safe=False)