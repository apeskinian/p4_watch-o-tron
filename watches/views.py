from django.shortcuts import render, get_object_or_404, redirect
from .models import Watch, WatchList
from .forms import WatchForm


def home(request, list_name='Collection'):
    if request.user.is_authenticated:
        watches = Watch.objects.filter(
            owner=request.user,
            list_name__list_name=list_name
        )
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

def add_watch(request):
    print('add_watch starting')
    if request.user.is_authenticated:
        if request.method == 'POST':
            print('POST has been found...')
            form = WatchForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.owner = request.user
                form.save()
                return redirect('home')
        else:
            context = {
                "watch_form": WatchForm()
            }
            return render(request, 'watches/add_watch.html', context)
    else:
        return render(request, 'account/login.html')