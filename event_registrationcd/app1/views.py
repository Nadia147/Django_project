from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#@login_required(login_url='login')
'''def HomePage(request):
    return render(request, 'home.html')'''
@login_required(login_url='login')
def HomePage(request):
    # Pass the user object to the template
    user = request.user
    context = {'user': user}
    return render(request, 'home.html', context)

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # Check if a user with the same username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username is already taken. Please choose a different username.')
            return render(request, 'signup.html')

        # Continue with user creation if the username is unique
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    else:
        return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
