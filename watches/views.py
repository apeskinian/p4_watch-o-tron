from django.shortcuts import render, get_object_or_404

def home(request):
    if request.user.is_authenticated:
        return render(request, 'watches/home.html')
    else:
        return render(request, 'account/login.html')
    
