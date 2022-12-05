from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Leaders


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    team=Leaders.objects.all()
    return render(request,"index.html",{'result':obj,'res':team})
