from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Addresses
from .serializers import AddressesSerializer
from django.contrib.auth import authenticate


# Create your views here.
@csrf_exempt
def addresses(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):

    object1 = Addresses.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AddressesSerializer(data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(object1, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    #
    elif request.method == 'DELETE':
        object1.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        # print('리퀘스트' + str(request.body))
        id = request.POST.get('userid', '')
        pw = request.POST.get('userpw', '')
        # print(id,pw)
        result = authenticate(username=id, password=pw)
        if result:
            print('성공')
            return render(request, 'addresses/success.html')
        else:
            print('실패')
            return render(request, 'addresses/fail.html')
    return render(request, 'addresses/login.html')

