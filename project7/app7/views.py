from django.shortcuts import render
from django.shortcuts import HttpResponse
def showindex(request):
    return render(request,"index.html")

def showdetails(request):
    idno=request.POST.get('t1')
    name=request.POST.get("t2")
    salary=request.POST.get("t3")
    return HttpResponse(idno+name+salary)