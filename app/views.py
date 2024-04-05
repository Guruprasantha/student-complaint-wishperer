from django.shortcuts import render,redirect,HttpResponse
from .models import *
from datetime import datetime

# Create your views here.

def home(request):
    return render(request,'index.html')
def homepage(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        mobno=request.POST.get('mobno')
        email=request.POST.get('email')
        pwrd=request.POST.get('pword')
        reg=Register(uname=uname,mobno=mobno,email=email,pwrd=pwrd)
        reg.save()
        return redirect('login')

    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pwrd=request.POST.get('pwrd')
        try:
            user=Register.objects.get(uname=uname)
            if user.pwrd==pwrd:
                print("First line ")
                request.session['username']=uname
                print("hello")
                return render(request,'home.html',{'session':request.session['username']})
            else:
                print("incorrect")
                data = {'status': "Incorrect Password!!!"}
                return render(request,'login.html',context=data)
        except:
            data = {'status': "No user found please register!!!"}
            return render(request,'login.html',context=data)

    return render(request,'login.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return render(request,'index.html')

def comreg(request):
    if request.method=='POST':
        name=request.session['username']
        mobno=request.POST.get('mobno')
        comcat=request.POST.get('comcat')
        comdt=datetime.now()
        comdis=request.POST.get('comdis')
        acta='Pending'
        
        comr=pcm(name=name,mobno=mobno,comcat=comcat,comdt=comdt,comdis=comdis,acta=acta)
        comr.save()
        return redirect('homepage')
    return render(request,'pcm.html')

def viewpcm(request):
    if 'username' in request.session:
        d=pcm.objects.filter(name=request.session['username'])
        print(d)
        data={'data':d}
        return render(request,'viewpcm.html',context=data)

def details(request,id):
    data=pcm.objects.get(id=id)
    print(data.comcat)
    print(data.comdis)
    view=Actiontake.objects.get(name=data.name,comdis=data.comdis)
    print(view.actiondate,view.acta,view.actionname)
    context={
        'i':view,
    }
    return render(request,'detailpcm.html',context)

def adminlogin(request):
    if request.method=='POST':
        user=request.POST.get('username')
        passw=request.POST.get('password')
        try:
            user=adminl.objects.get(username=user)
            if user.password==passw:
                return redirect('admina')
            else:
                print("incorrect")
                data = {'status': "Incorrect Password!!!"}
                return render(request,'adminlogin.html',context=data)
        except:
            data = {'status': "No user found please enter valid details!!!"}
            return render(request,'adminlogin.html',context=data)
    return render(request,'adminlogin.html')    

def admina(request):
    data=pcm.objects.all()
    li=[]
    for i in data:
        li.append(i)
    z=len(li)

    pending=pcm.objects.filter(acta='Pending')
    lia=[]
    for i in pending:
        lia.append(i)
    pe=len(lia)

    act=pcm.objects.filter(acta='Action Taken')
    lii=[]
    for i in act:
        lii.append(i)
    ac=len(lii)
    context={
        'data':data,
        'tc':z,
        'pending':pe,
        'acttaken':ac,
    }
    return render (request,'admin.html',context)

def action(request,id):
    if request.method=='POST':
        actionname=request.POST.get('actionname')
        aboutaction=request.POST.get('aboutaction')
        data=pcm.objects.get(id=request.POST.get('actionid'))
        ad=Actiontake()
        ad.name=data.name
        ad.mobno=data.mobno
        ad.comcat=data.comcat
        ad.comdt=data.comdt
        ad.comdis=data.comdis
        ad.acta='Action Taken'
        ad.actionname=actionname
        ad.actiondis=aboutaction
        ad.actiondate=datetime.now()
        data.acta='Action Taken'
        data.save()
        ad.save()
    
        return redirect('admina')
    data=pcm.objects.get(id=id)
    print(data)
    context={
        'udata':data
    }
    return render(request,'action.html',context)


def complaintstaken(request):
    data=Actiontake.objects.all()
    context={
        'data':data
    }
    return render(request,'comdata.html',context)
    
