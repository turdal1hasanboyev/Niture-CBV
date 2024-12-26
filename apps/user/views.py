from django.views import View # view class
from django.shortcuts import render, redirect # shortcuts
from django.contrib.auth import authenticate, login, logout # login logout authenticate
from django.contrib import messages # message
from django.contrib.auth.decorators import login_required # login majburiy qilish
from django.utils.decorators import method_decorator # logout uchun
from .models import CustomUser # model


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Error! The password or username was entered incorrectly')
            return redirect('login')
        
login_as_view = LoginView.as_view()
        

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have successfully logged out!')
        return redirect('home')
    
logout_as_view = LogoutView.as_view()


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            image=image,
            description=description,
            gender=gender,
            birthday=birthday,
        )
        user.save()
        messages.success(request, 'You have successfully registered!')
        # login(request, user)
        # return redirect('home') # to'g'ridan togri login qiladi
        return redirect('login')
    # Login sahifasiga redirect qilib yuboradi

register_as_view = RegisterView.as_view()
    