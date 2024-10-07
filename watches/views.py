from django.shortcuts import render, get_object_or_404
from .models import Watch, WatchList


def home(request, list_name='Collection'):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(owner=request.user)
        lists = WatchList.objects.values_list('list_name', flat=True)
        current_list = list_name
        context = {
            'watches': watches,
            'lists': lists,
            'current_list': current_list
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, 'account/login.html')