from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=764197b2d0a6b547cda5451c97546cf4').read()
        print(res)
        json_data=json.loads(res)
        data={
            "code":str(json_data['sys']['country']),
            "coor":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "tem":str(json_data['main']['temp'])+'K',
             "tem1":int(json_data['main']['temp'])-273,
             "tem2":int(json_data['main']['feels_like'])-273,
            
            "pre":str(json_data['main']['pressure']),
            "hum":str(json_data['main']['humidity'])
           


        }

    else:
        city=''
        data={}
    return render(request,'index.html',{'city':city,'data':data})