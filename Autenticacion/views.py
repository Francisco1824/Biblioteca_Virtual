from re import A
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout ,authenticate
from django.contrib import messages

# Create your views here.
class V_Registro(View):
    
    def get (self,request):
        form= UserCreationForm()
        return render (request, 'registro.html', {'form': form})
    
    def post (self,request):
        form= UserCreationForm(request.POST)
        
        if form.is_valid():
        
            usuario= form.save()
        
            login (request,usuario)
        
            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                
            return render (request, 'registro.html', {'form': form})
        
def Cerrar_Sesion(request):
    logout(request)
    return redirect('home')

def Login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get("username")
            contrasenia= form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=contrasenia)
            if usuario is not None:
                login (request,usuario)
                return redirect('home')
            else:
                messages.error(request,"Usuario no valido")
        else:
                messages.error(request,"Informacion incorrecta")       
    
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})