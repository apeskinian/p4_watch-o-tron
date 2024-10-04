from django.shortcuts import render, get_object_or_404
from .models import Watch, WatchList

def home(request):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(owner=request.user)
        context = {
            'watches': watches
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, 'account/login.html')
    
