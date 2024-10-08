from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Watch, WatchList
from .forms import WatchForm


@login_required(login_url='accounts/login')
def home(request, list_name='Collection'):
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


@login_required(login_url='accounts/login')
def add_watch(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('home')
    else:
        cancel_url = request.META.get('HTTP_REFERER', '/')
        context = {
            "watch_form": WatchForm(),
            "cancel_url": cancel_url
        }
        return render(request, 'watches/add_watch.html', context)


@login_required(login_url='accounts/login')
def delete_watch(request, watch_id):
    return_url = request.META.get('HTTP_REFERER', '/')
    watch = get_object_or_404(Watch, id=watch_id)
    watch.delete()
    return redirect(return_url)
