from django.shortcuts import render, redirect
from .forms import fo
from .models import too


# Create your views here.
def index(request):
    obj=too.objects.all()
    if request.method=='POST':
        name=request.POST.get('ent',)
        priority=request.POST.get('prior',)
        date=request.POST.get('date',)
        new=too(name=name,priority=priority,date=date)
        new.save()
        return redirect('/')

    return render(request,'index.html',{'obj':obj})

def delete(request,id):
    tas = too.objects.get(id=id)
    if request.method=='POST':

       tas.delete()
       return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tas=too.objects.get(id=id)
    f=fo(request.POST or None,instance=tas)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'task':tas,'form':f})
