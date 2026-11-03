from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
# Create your views here.

def singleobj(request):
   
    data =  Person.objects.get(id=1)    
    serializer= PersonSerializer(data)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type= 'application/json')
        
@csrf_exempt
def multipleobj(request):
    if request.method == 'POST':
            json= request.body
            stream= io.BytesIO(json)
            parsed_data =JSONParser().parse(stream)
            serializer = PersonSerializer(data=parsed_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"Created": "successfull"},status= status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
            
    data = Person.objects.all()
    serializer = PersonSerializer(data, many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type= 'application/json')