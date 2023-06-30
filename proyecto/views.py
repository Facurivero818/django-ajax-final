from django.shortcuts import render
from django.http import JsonResponse
import json

def vista(request):

    return render(request,"index.html")

def calculo(request):

    context ={}

    if request.method == "POST":

        data = json.loads(request.body)
        var = data.get('operacion', '')
        var = var.replace(" ","")
        largo= len(var)

        if var[largo-1] == ";" and (";" not in var[:-1]) and not any(digito.isalpha() for digito in var) and not any(var[i-1].isdigit() == var[i].isdigit() for i in range(1, largo-1)) and var[0]!= "-" and var[-2].isdigit() and not any(map(lambda x: x in var, ["(",")"])):
        # SI HAY UN ; FINAL Y NO HAY LETRAS Y NO HAY 2 DIGITOS JUNTOS Y NO HAY UN SIGNO NEGATIVO EN LA PRIMERA POSICION (NUMERO NEGATIVO) Y EL ANTEULTIMO CARATER NO SEA UN OPERADOR Y NO HAY PARENTESIS    
            var = var[:-1]
            try:
                resultado = round(eval(var),2)

            except ZeroDivisionError:
                resultado = "No se puede divir por 0"

        else:
            resultado = "La cadena no cumple con lo solicitado"

        context["respuesta"] = resultado
        return JsonResponse(context)
    
    elif request.method == "GET":
        context = {"respuesta":"Solicitud incorrecta"}
        return JsonResponse(context)
    
    else: 
        context = {"respuesta":"Error al recibir la peticion"}
        return JsonResponse(context)