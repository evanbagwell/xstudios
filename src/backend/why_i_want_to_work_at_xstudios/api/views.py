from django.shortcuts import render
from django.http import JsonResponse

def return_33(request):
    data = {'value': 33}
    return JsonResponse(data)
