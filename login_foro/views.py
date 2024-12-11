from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.

def base(request):
    return render (request,'base.html')

def login(request):
    return render (request,'login.html')



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Guardar el usuario y autenticarlo directamente
            user = form.save()
            
            # Autenticar al usuario después de crearlo
            authenticated_user = authenticate(
                username=form.cleaned_data.get('username'), 
                password=form.cleaned_data.get('password1')
            )

            # Iniciar sesión
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('foro_app:Home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'Home.html', {
        'user': request.user,
        'role': request.user.get_full_role()
    })