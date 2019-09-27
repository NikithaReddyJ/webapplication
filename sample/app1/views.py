from django.shortcuts import render
from .models import table,table1,table2,user
from django.http import HttpResponseRedirect
# Create your views here.
def app1view(request):
    return render(request, 'land.html')
def dashboardview(request):
    return render(request, 'dashboard.html')
def Tview(request):
    c=table1.objects.all()
    e=table2.objects.all()
    return render(request, 'T.html')
def newframeview(request):
    a=table.objects.all()
    return render(request, 'newframe.html',{'alldata':a})
def userprofileview(request):
    return render(request, 'userprofile.html')
def ftableview(request):
    b=table.objects.all()
    return render(request, 'table.html',{'alldata':b})
def ftable1view(request):
    d=table1.objects.all()
    return render(request, 'table1.html',{'data':d})
def ftable2view(request):
    f=table2.objects.all()
    return render(request, 'table2.html',{'data':f})
def deleteview(request,k_id):
    d=table1.objects.get(id = k_id)
    x=table1.objects.all()
    d.delete()
    return render(request, 'table1.html',{'data':x})
def updateview(request,m_id):
    m=table1.objects.get(id=m_id)
    return render(request, 'update.html',{'datat':m})
def update(request,m_id):
    y=table1.objects.get(id = m_id)
    y.content=request.POST.get('content')
    m=table1.objects.all()
    y.save()
    return HttpResponseRedirect( "/table1/ftable1/" )

def userview(request):
    a=request.POST['company']
    item=user(company=a)
    item.save()
    b=request.POST['username']
    item1=user(company=b)
    item1.save()
    c=request.POST['email']
    item2=user(company=c)
    item2.save()
    d=request.POST['firstname']
    item3=user(company=d)
    item3.save()
    e=request.POST['lastname']
    item4=user(company=e)
    item4.save()
    f=request.POST['city']
    item5=user(company=f)
    item5.save()
    g=request.POST['country']
    item6=user(company=g)
    item6.save()
    h=request.POST['postalcode']
    item7=user(company=h)
    item7.save()
    return HttpResponseRedirect("/user/")
