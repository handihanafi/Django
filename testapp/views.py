from urllib import request
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.views import View
# from django.contrib import messages

# Create your views here.
def home(requset):
    records = Record.objects.all()

    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(requset, user)
            messages.success(requset, "You Have been Logged In!")
            return redirect('home')
        else:
            messages.success(requset, "There Was An Error Logged In, Please Try Again")
            return redirect('home')
    else:
        return render(requset, 'home.html', {'records': records})

# class HomeView(View):
#     template_name = 'home.html'

#     def get(self, request):
#         return render(request, self.template_name, {})

#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, "You have been logged in!")
#             return redirect('home')
#         else:
#             messages.error(request, "There was an error logging in. Please try again.")
#             return redirect('home')

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('home')
        else:
            # Pass the existing form with errors to the template
            return render(request, 'register.html', {'form': form})
    elif request.method == 'GET':
        form = SignUpForm()
    else:
        # Handle other request methods if necessary
        return HttpResponseBadRequest("Invalid request method")

    return render(request, 'register.html', {'form': form})