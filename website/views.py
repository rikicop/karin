from django.shortcuts import render
from .models import Contact, Post, Equipo
    

def home(request):
    items = Post.objects.all()
    equipos = Equipo.objects.all()
    if request.method =="POST":
        name_form = request.POST['namef']
        email_form = request.POST['emailf']
        message_form = request.POST['messagef']
        #Insertar el objeto
        Contact.objects.create(name=name_form,email=email_form,message=message_form)

        return render(request, 'home.html',{'items':items, 'equipos':equipos})
          
    else:
        
        return render(request, 'home.html',{'items':items, 'equipos':equipos})

    return render(request, 'home.html', {'items':items,'equipos':equipos})

""" def post(request):
    items = Post.objects.all()
    return render(request, 'home.html', {'items':items})
 """
def details(request):
    return render(request, 'details.html', {})

def inmuebles(request):
    return render(request, 'inmuebles.html', {})