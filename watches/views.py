from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Watch, WatchList, WatchMovement
from .forms import WatchForm, MovementForm, ListForm


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
def edit_watch(request, watch_id):
    cancel_url = request.META.get('HTTP_REFERER', '/')
    watch = get_object_or_404(Watch, id=watch_id)
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            new_list = form.instance.list_name.list_name
            return redirect('watch_list', list_name=new_list)
    else:
        context = {
            "watch_form": WatchForm(instance=watch),
            "cancel_url": cancel_url,
            "watch": watch
        }
        return render(request, 'watches/edit_watch.html', context)
    

@login_required(login_url='accounts/login')
def purchase_watch(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    collection_list = get_object_or_404(WatchList, list_name='Collection')
    watch.list_name = collection_list
    watch.save()
    return redirect('watch_list', 'Collection')


@login_required(login_url='accounts/login')
def delete_watch(request, watch_id):
    return_url = request.META.get('HTTP_REFERER', '/')
    watch = get_object_or_404(Watch, id=watch_id)
    watch.delete()
    return redirect(return_url)


@staff_member_required(login_url='accounts/login')
def settings(request):
    





    movements = WatchMovement.objects.all()
    list_names = WatchList.objects.all()
    context = {
        'movement_form': MovementForm(),
        'list_form': ListForm(),
        'movements': movements,
        'list_names': list_names
    }
    return render(request, 'watches/settings.html', context)
