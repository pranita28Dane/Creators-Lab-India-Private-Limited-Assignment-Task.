from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from myapp.models import Document
from myapp.forms import DocumentForm


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')

    else:
        f = CustomUserCreationForm()

    return render(request, 'app/register.html', {'form': f})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or any other desired page

@login_required
def home(request):
    documents = Document.objects.all()
    return render(request, 'app/home.html', {'documents': documents})


@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'app/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'app/simple_upload.html')

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'app/model_form_upload.html', {'form': form})

