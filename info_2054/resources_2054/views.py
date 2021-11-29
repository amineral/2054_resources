from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer, InteractiveBoard, Department
from .filters import ComputerFilter
from .forms import CheckBoxFilter

def index(request):
    return render(request, 'resources_2054/index.html')

def main_page(request, dp):
    school = Department.objects.get(number=dp)
    return render(request, 'resources_2054/main.html', {"school" : school})

def comps(request, dp):
    school = Department.objects.get(number=dp)
    comps = Computer.objects.filter(dp=school)
    f = ComputerFilter(request.GET, queryset=comps)
    form = CheckBoxFilter()
    context = {
        "comps" : comps,
        "filter" : f,
        "form" : form,
    }
    return render(request, 'resources_2054/comps.html', context)

def boards(request):
    all_boards = InteractiveBoard.objects.all()
    context = {"boards" : all_boards}
    return render(request, 'resources_2054/boards.html', context)

def proceed_filter(request):
    print(request.GET)
    return HttpResponse("OK")
