from django.shortcuts import render

# Create your views here.

def textdata(request):
    return render(request,'textdata.html')