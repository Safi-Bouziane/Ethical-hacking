from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import GebruikerRegistratieForm, GebruikersAuthenticatieForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def registreer(request):
    if request.method == 'GET':
        return render(request, 'registreer.html', {'form':GebruikerRegistratieForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registreer.html', {'form':GebruikerRegistratieForm, 'error':'Gebruikersnaam is reeds in gebruik. Kies een nieuwe.'})
        else:
            return render(request, 'registreer.html', {'form':GebruikersAuthenticatieForm, 'error':' Wachtwoorden matchen niet'})

@login_required
def loguit(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form':GebruikersAuthenticatieForm})
    else:
        user = authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'form': GebruikersAuthenticatieForm,'error': 'Gebruikersnaam en wachtwoord matchen niet'})
        else:
            login(request,user)
            return redirect('home')