from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, FormRecord
from .models import Record

from django.http import HttpResponse

def home(request):

    records = Record.objects.all()

    #request c’est l’objet qui contient toutes les informations sur la requête de l’utilisateur.

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            login(request, user)
            messages.success(request, "vous etes connecter")
            return redirect('home')
        else:
            messages.success(request, "Error Login...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records' : records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Vous etes deconnecter")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = get_object_or_404(Record, id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'vous devez vous connecter')
        return redirect('home')
    
def delete_record(request, pk):

    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record Supprimer avec success")
        return redirect('home')
    else:
        messages.success(request, "Vous devez vous connecter")
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FormRecord(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Posté avec success')
                return redirect('home') 
        else:
            return render(request, 'forms.html', {'form':FormRecord})
    else:
        messages.success(request, 'Vous devez vous connecter...')
        return redirect('home')
    
    return render(request, 'forms.html', {'form':FormRecord})


def edit_record(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_record = Record.objects.get(id=pk)
            form = FormRecord(request.POST or None, instance=current_record) 
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Modifier avec success')
                return redirect('home')
            return render(request, 'forms.html', {'form':form})
    else:
        messages.success(request, 'Vous devez vous connecter')
        return redirect('home')
    form = FormRecord(request.POST or None, instance=Record.objects.get(id=pk))
    return render(request, 'forms.html', {'form': form, 'record': Record.objects.get(id=pk)})