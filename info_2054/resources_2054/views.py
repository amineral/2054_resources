from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Computer, InteractiveBoard, Department
from .forms import ComputerFilter
from .serializers import ComputerSerializer


def index(request):
    return render(request, 'resources_2054/index.html')

def main_page(request, dp):
    school = Department.objects.get(number=dp)
    return render(request, 'resources_2054/main.html', {"school" : school})

def comps(request, dp):
    filtered = None
    if request.method == "GET" and request.GET:
        form = ComputerFilter(request.GET)
        if form.is_valid():
            comp_type = request.GET["type"]
            owner = request.GET["owner"]
            if comp_type == "all":
                filtered = Computer.objects.all()
            else:
                filtered = Computer.objects.filter(owner__contains=owner, comp_type__contains=comp_type)
    else:
        form = ComputerFilter()
    context = {
        "form" : form,
        "dp" : dp,
        "filtered" : filtered,
    }
    return render(request, 'resources_2054/comps.html', context)

def boards(request):
    all_boards = InteractiveBoard.objects.all()
    context = {"boards" : all_boards}
    return render(request, 'resources_2054/boards.html', context)

@api_view(['GET', 'POST'])
def comp_list(request):
    if request.method == "GET":
        comps = Computer.objects.all()
        serializer = ComputerSerializer(comps, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return HttpResponse("POST method temporarily unavailable")
    

@api_view(['GET', 'POST'])
def comp_details(request, pk):
    if request.method == "GET":
        comp = Computer.objects.get(pk=pk)
        serializer = ComputerSerializer(comp)
        return Response(serializer.data)
    return HttpResponse("POST method temporarily unavailable")
