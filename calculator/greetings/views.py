from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.views import Response
from datetime  import datetime

class goodmorningviews(APIView):
    def get(self,request,*args,**kw):
        return Response('Hello Goodmorning')
    
class goodeveningviews(APIView):
    def get(self,request,*args,**kw):
        return Response('Hello Goodevening')
    
class Todayview(APIView):
    def get(self,request,*args,**kw):
        time_now=datetime.now()
        return Response(data=time_now)
    
class Addview(APIView):
    def post(self,request,*args,**kw):
        print(request.data)
        a=request.data.get('num1')
        b=request.data.get('num2')
        c=int(a)+int(b)
        return Response(data=c)
    
class subView(APIView):
    def post(self,request,*args,**kw):
        print(request.data)
        a=int(request.data.get('num1'))
        b=int(request.data.get('num2'))
        if a>b:
            c=a-b
        else:
            c=b-a
            return Response(data=c)
        

class cubeView(APIView):
    def post(self,request,*args,**kw):
        print(request.data)
        a=int(request.data.get('num1'))
        c=a*a*a
        return Response(data=c)