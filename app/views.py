from django.shortcuts import render,HttpResponse,redirect
import requests
import datetime
from django.contrib import messages

def home(request):


    if "city" in request.POST:
        city=request.POST['city']
    else:
        city='Bangalore'

    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6b820829125e826347493bbac82bc359"
    PARAMS={'units':'metric'} 

    # API_KEY= "AIzaSyDRLLdAh1jxseQbHBZmQDnoQjwdu8z3fLgp"
    # SEARCH_ENGINE_ID="c1b9cb5756f1d4802"

    # query = city + "1920x1080" #fix image size
    # page = 1                  
    # start = (page-1)*10+1
    # searchType = 'image'
    # city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    # data=requests.get(city_url).json()
    # count=1
    # search_items= data.get("items")
    # image_url=search_items[1]["link"]

    # Make a request to the Unsplash API to get city images
    access_key = 'fvmd0kWtqAo3ot5IAnEQCrhDdNgIPsrMO1uURubIXx4'
    endpoint = f'https://api.unsplash.com/search/photos'
    params = {
        'query': city,
        'client_id': 'fvmd0kWtqAo3ot5IAnEQCrhDdNgIPsrMO1uURubIXx4',
    }

    data = requests.get(endpoint, params=params).json()

    # Extract image URLs from the API response
    image_urls = []
    for photo in data['results']:
        image_urls.append(photo['urls']['raw'])
    if len(image_urls) == 0:    
        image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'
    elif len(image_urls) > 0:
        image_url = image_urls[0]




    try:
        data=requests.get(url,PARAMS).json()

        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
        day=datetime.date.today()

        return render(request,"app/index.html",{'city':city,'description':description,'icon':icon,'temp':temp,'day':day,"except_occured":False,"image_url":image_url})
    
    except KeyError:
        Exception_occured=True
        messages.error(request,"Enter data is not Available to API.")
        day=datetime.date.today()

        return render(request,"app/index.html",{'city':'Bangalore','description':'clear Sky','icon':'01d','temp':25,'day':day,'exception_occured':True})

    
    
 
