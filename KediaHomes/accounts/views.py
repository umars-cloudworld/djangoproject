from accounts.managers import CustomUserManager
from django.shortcuts import render, redirect
from django.utils.decorators import decorator_from_middleware
from .middleware import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def ValidateCustomer():
    error_message = None
    pass


@decorator_from_middleware(UserLoginMiddleware)
def login_view(request, form=None):
    redirect_url = request.GET['next'] if 'next' in request.GET else '/'
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            #validation

            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(redirect_url)
            return render(request, 'login.html', {'error': 'Invalid User'})
        else:
            error_message = "Please enter valid details"
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html')


@decorator_from_middleware(RegisterMiddleware)
def register_view(request, form=None):
    if request.method == "POST":
        # edits validation
        name = request.POST.get('name')
        email = request.POST.get('email')
        code = request.POST.get('code')
        mobile_raw = request.POST.get('mobile')
        mobile_validation = code + '-' + mobile_raw
        print(mobile_validation)
        password = request.POST.get('password')
        if not email:
            error_message = "Please enter email address!"
            return render(request, "register.html", {'error_message':error_message})
        elif not mobile_raw:
            error_message = "Please enter phone number!"
            return render(request, "register.html", {'error_message':error_message})
        # elif len(mobile_raw) < 10:
        #     error_message = "Please enter a valid mobile number!"
        #     return redirect(request, "register.html", {'error_message':error_message})
        elif not password:
            error_message = "Please enter password!"
            return render(request, "register.html", {'error_message':error_message})
        elif User.emailExists(email):
            error_message = "Email already registered!"
            return render(request, "register.html", {'error_message':error_message})
        elif User.mobileExists(mobile_validation):
            error_message = "Phone number already registered!"
            return render(request, "register.html", {'error_message':error_message})

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            mobile = form.cleaned_data['code'] + '-' + str(form.cleaned_data['mobile'])
            user = User.objects.create_user(name=name, email=email, password=password, mobile=mobile)
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form},{'error':'Invalid details'})
    return render(request, 'register.html')


@decorator_from_middleware(ForgetPasswordMiddleware)
def forget_password(request, form=None):
    if request.method == "POST":
        if form.is_valid():
            return render(request, 'forgot_password.html')
        else:
            return render(request, 'forgot_password.html', {'form': form})
    return render(request, 'forgot_password.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')


@login_required()
@decorator_from_middleware(ProfileMiddleware)
def profile_view(request, form=None):
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'profile.html')
