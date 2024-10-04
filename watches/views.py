from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Watch, WatchList


def collection(request):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(owner=request.user)
        collection = 'Collection'
        context = {
            'watches': watches,
            'collection': collection
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, 'account/login.html')

    
def wishlist(request):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(owner=request.user)
        collection = 'Wish List'
        context = {
            'watches': watches,
            'collection': collection
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, 'account/login.html')