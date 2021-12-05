from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Computer, InteractiveBoard, Department
from .forms import ComputerFilter

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
            filtered = Computer.objects.filter(comp_type=comp_type, owner=None)
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
