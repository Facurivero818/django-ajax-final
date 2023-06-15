from django.shortcuts import render
from django.http import JsonResponse
import json

def vista(request):
    return render(request,"index.html")

def calculo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        context ={}
        context['respuesta'] = data.get('operacion', '')
        return JsonResponse(context)
    
    elif request.method == "GET":
        context = {"respuesta":"casi bien"}
        return JsonResponse(context)
    
    else: 
        context = {"respuesta":"Error al recibir la peticion"}
        return JsonResponse(context)