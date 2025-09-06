from django.shortcuts import render, redirect
from .models import login 
from .forms import LoginForm  


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = login(username=username, passwords=password)
            data.save()

    return render(request, 'pages/form.html', {'lf': LoginForm()})






# 3-------------------------------------------

# from django.shortcuts import render, redirect
# from .models import login 
# from .forms import LoginForm  


# def home(request):
#     return render(request, 'pages/home.html')


# def about(request):
#     return render(request, 'pages/about.html')

    
# def form(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = LoginForm()

#     return render(request, 'pages/form.html', {'lf': form})