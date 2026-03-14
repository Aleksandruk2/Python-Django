
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):

    if request.method == 'POST':
        # print("---Зберігаємо дані користувача---")
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                if 'email' in form.cleaned_data:
                    user.username = form.cleaned_data['email']
                image = request.FILES.get("image")
                if image:
                    user.image_small = image
                    user.image_medium = image
                    user.image_large = image
                user.save()
                login(request, user)
                return redirect('homepage')
            except Exception as e:
                messages.error(request, f"Щось пішло не так: {str(e)}")
        else:
            messages.success(request, 'Виправте помилки у формі')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = CustomUserLogin(data = request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = CustomUserLogin()
    return render(request, "login.html", {'form': form})

def user_logout(request):
    logout(request)
    return redirect('homepage')