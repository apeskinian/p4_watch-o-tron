from django.shortcuts import render, get_object_or_404
from .models import Watch, WatchList


# working code
def collection(request):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(owner=request.user)
        lists = WatchList.objects.all()
        current_list = 'Collection'
        context = {
            'watches': watches,
            'current_list': current_list,
            'lists': lists
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, 'account/login.html')

    
def wishlist(request):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(owner=request.user)
        lists = WatchList.objects.all()
        current_list = 'Wish List'
        context = {
            'watches': watches,
            'current_list': current_list,
            'lists': lists
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, 'account/login.html')