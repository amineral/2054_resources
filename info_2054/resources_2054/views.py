from django.http.response import HttpResponsePermanentRedirect, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Computer, InteractiveBoard, Department
from .forms import ComputerFilter, AddComputerForm, AuthForm
from .serializers import ComputerSerializer, InteractiveBoardSerializer


def auth_page(request):
    if request.user.is_authenticated == True:
        return redirect('index')
    if request.method == "POST":
        form = AuthForm(request.POST)
        username = request.POST["login"]
        password = request.POST["password"]
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = "Неправильный логин или пароль"
                return render(request, 'resources_2054/auth.html', {"form" : AuthForm, "message" : message})
        else:
            return HttpResponse("form not valid")
    else:
        form = AuthForm()
    return render(request, 'resources_2054/auth.html', {"form" : form, "message" : None})

@login_required
def logout_page(request):
    logout(request)
    return redirect('auth_page')

@login_required
def index(request):
    return render(request, 'resources_2054/index.html',)

@login_required
def main_page(request, dp):
    school = Department.objects.get(number=dp)
    return render(request, 'resources_2054/main.html', {"school" : school})

@login_required
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

@login_required
def comp_details(request, pk):
    comp = Computer.objects.get(pk=pk)
    context = {
        "comp" : comp,
    }
    return render(request, 'resources_2054/comp_details.html', context)

@login_required
def boards(request, dp):
    all_boards = InteractiveBoard.objects.all()
    context = {"boards" : all_boards}
    return render(request, 'resources_2054/boards.html', context)

@login_required
def board_details(request, pk):
    board = InteractiveBoard.objects.get(pk=pk)
    context = {
        "board" : board,
    }
    return render(request, 'resources_2054/board_details.html', context)

@login_required
def add_device(request, device):
    if device == 1:
        if request.GET:
            comp_type = request.GET["comp_type"]
            brand = request.GET["brand"]
            serial_number = request.GET["serial_number"]
            owner = request.GET["owner"]
            dp = Department.objects.get(number=int(request.GET["dp"]))
            new_comp = Computer(
                comp_type=comp_type,
                brand=brand,
                serial_number=serial_number,
                owner=owner,
                status="OK",
                dp=dp,
            )
            new_comp.save()
            messages.success(request, 'Устройство добавлено')
            return redirect('index')
    if device == 2:
        return HttpResponse("in work")
    context = {
        "device" : device,
    }
    return render(request, 'resources_2054/add_device.html', context)


# ---------- API VIEWES -------------------------------------------- 

def main_api(request):
    api_list = {
        "/api/comps" : "computers list",
        "/api/comps/<int:id>" : "computer details",
    }
    return JsonResponse(api_list)

@api_view(['GET', 'POST'])
def comp_list_api(request):
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
    

@api_view(['GET', 'POST'])  # change to GET PUT DELETE
def comp_details_api(request, pk):
    if request.method == "GET":
        comp = Computer.objects.get(pk=pk)
        serializer = ComputerSerializer(comp)
        return Response(serializer.data)
    return HttpResponse("POST method temporarily unavailable")


@api_view(['GET', 'POST'])
def board_list_api(request):
    if request.method == "GET":
        boards = InteractiveBoard.objects.all()
        serializer = InteractiveBoardSerializer(boards, many=True)
        return Response(serializer.data)
        
    elif request.method == "POST":
        serializer = InteractiveBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return HttpResponse("POST method temporarily unavailable")
    

@api_view(['GET', 'POST']) # change to GET PUT DELETE
def board_details_api(request, pk):
    if request.method == "GET":
        board = InteractiveBoard.objects.get(pk=pk)
        serializer = InteractiveBoardSerializer(board)
        return Response(serializer.data)
    return HttpResponse("POST method temporarily unavailable")
