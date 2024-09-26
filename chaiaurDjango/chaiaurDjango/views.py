
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    return HttpResponse("Hello, world. You're at the polls about.")



def contact(request):
    return HttpResponse("Hello, world. You're at the polls contect.")


