from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['phone']
        msg = request.POST['msg']
        obj=Portfolio(name=name,email=email,phone=contact,message=msg)
        obj.save()
    return render(request,"index.html",{})