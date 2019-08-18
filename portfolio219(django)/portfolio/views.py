from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.GET['name']

        email = request.GET['email']
        contact = request.GET['phone']
        msg = request.GET['msg']
        obj=Portfolio(name=name,email=email,phone=contact,message=msg)
        obj.save()
    return render(request,"index.html",{})