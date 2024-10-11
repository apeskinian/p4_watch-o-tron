from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
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
    viewmessage = f'Viewing {list_name}'
    messages.add_message(request, messages.INFO, viewmessage)
    return render(request, 'watches/home.html', context)


@login_required(login_url='accounts/login')
def add_watch(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            new_list = form.instance.list_name.list_name
            return redirect('watch_list', list_name=new_list)
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
    if request.method == 'POST':
        if 'movement-form' in request.POST:
            form = MovementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('settings')
        elif 'list-form' in request.POST:
            form = ListForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('settings') 
    movements = WatchMovement.objects.all()
    lists = WatchList.objects.values_list('list_name', flat=True)
    list_names = WatchList.objects.all()   
    context = {
        'movement_form': MovementForm(),
        'list_form': ListForm(),
        'movements': movements,
        'lists': lists,
        'list_names': list_names
    }
    return render(request, 'watches/settings.html', context)


@staff_member_required(login_url='accounts/login')
def edit_movement(request, movement_id):
    cancel_url = request.META.get('HTTP_REFERER', '/')
    movement = get_object_or_404(WatchMovement, id=movement_id)
    associated = movement.watch_movement.count()
    if request.method == 'POST':
        form = MovementForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        movements = WatchMovement.objects.all()
        lists = WatchList.objects.values_list('list_name', flat=True)
        list_names = WatchList.objects.all()   
        context = {
            'cancel_url': cancel_url,
            'associated': associated,
            'edit_form': MovementForm(instance=movement),
            'movement_form': MovementForm(),
            'list_form': ListForm(),
            'movements': movements,
            'lists': lists,
            'list_names': list_names
        }
        return render(request, 'watches/settings.html', context)


@staff_member_required(login_url='accounts/login')
def edit_list(request, list_id):
    cancel_url = request.META.get('HTTP_REFERER', '/')
    list_name = get_object_or_404(WatchList, id=list_id)
    associated = list_name.watch_list.count()
    if request.method == 'POST':
        form = ListForm(request.POST, instance=list_name)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        movements = WatchMovement.objects.all()
        lists = WatchList.objects.values_list('list_name', flat=True)
        list_names = WatchList.objects.all()   
        context = {
            'cancel_url': cancel_url,
            'associated': associated,
            'edit_form': ListForm(instance=list_name),
            'movement_form': MovementForm(),
            'list_form': ListForm(),
            'movements': movements,
            'lists': lists,
            'list_names': list_names
        }
        return render(request, 'watches/settings.html', context)


@staff_member_required(login_url='accounts/login')
def delete_movement(request, movement_id):
    
    return_url = request.META.get('HTTP_REFERER', '/')
    movement = get_object_or_404(WatchMovement, id=movement_id)
    associated = movement.watch_movement.count()

    movement.delete()
    messages.success(request, f'Movement "{movement}" has been deleted. {associated} watches have been affected by this.')
    return redirect(return_url)


@staff_member_required(login_url='accounts/login')
def delete_list(request, list_id):
    return_url = request.META.get('HTTP_REFERER', '/')
    list_name = get_object_or_404(WatchList, id=list_id)
    associated = list_name.watch_list.count()

    list_name.delete()
    messages.success(request, f'The list "{list_name}" has been deleted. {associated} watches have been affected by this.')
    return redirect(return_url)
