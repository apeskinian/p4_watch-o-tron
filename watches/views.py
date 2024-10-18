from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Watch, WatchList, WatchMovement
from .forms import WatchForm, MovementForm, ListForm
import datetime


@login_required(login_url='accounts/login')
def home(request, list_name='Collection'):
    lists = WatchList.objects.values_list('list_name', flat=True)
    if list_name in lists:
        watches = Watch.objects.filter(
            owner=request.user,
            list_name__list_name=list_name
        )
        lists = WatchList.objects.values_list('list_name', flat=True)
        current_list = list_name
        day = datetime.datetime.now()
        context = {
            'day': day.strftime('%w'),
            'date': day.strftime('%d'),
            'watches': watches,
            'lists': lists,
            'current_list': current_list
        }
        return render(request, 'watches/home.html', context)
    else:
        return render(request, '404.html')


@login_required(login_url='accounts/login')
def add_watch(request, origin):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            new_list = form.instance.list_name.list_name
            messages.success(request, f'Added {form.instance.make} watch to {new_list}.')
            return redirect('watch_list', list_name=new_list)
        else:
            errors = form.errors
            error_message = ''
            for field, error_list in errors.items():
                error_message += f'{field}: {', '.join(error_list)}.'
            messages.error(request, f'Failed to add watch. {error_message}.')
    else:
        context = {
            "origin": origin,
            "watch_form": WatchForm(),
        }
        return render(request, 'watches/add_watch.html', context)


@login_required(login_url='accounts/login')
def edit_watch(request, watch_id, origin):
    watch = get_object_or_404(Watch, id=watch_id)
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()

            new_list = form.instance.list_name.list_name
            messages.success(request, f'{watch.make} watch editted successfully.')
            return redirect('watch_list', list_name=new_list)
        else:
            errors = form.errors
            error_message = ''
            for field, error_list in errors.items():
                error_message += f'{field}: {', '.join(error_list)}.'
            messages.error(request, f'Failed to edit watch. {error_message}.')
    else:
        context = {
            "origin": origin,
            "watch_form": WatchForm(instance=watch),
            "watch": watch
        }
        return render(request, 'watches/edit_watch.html', context)


@login_required(login_url='accounts/login')
def purchase_watch(request, watch_id):
    try:
        watch = get_object_or_404(Watch, id=watch_id)
        collection_list = get_object_or_404(WatchList, list_name='Collection')
        watch.list_name = collection_list
        messages.success(request, f'{watch.make} watch moved to Collection.')
        watch.save()
    except Exception as e:
        messages.error(request, f'Error occured while moving watch to Colletction: {str(e)}')
    
    return redirect('watch_list', 'Collection')


@login_required(login_url='accounts/login')
def delete_watch(request, watch_id):
    try:
        return_url = request.META.get('HTTP_REFERER', '/')
        watch = get_object_or_404(Watch, id=watch_id)
        messages.info(request, f'{watch.make} watch deleted from {watch.list_name}.')
        watch.delete()
    except Exception as e:
        messages.error(request, f'Error occured while deleting watch: {str(e)}')
    
    return redirect(return_url)


@staff_member_required(login_url='accounts/login')
def staff_settings(request):
    if request.method == 'POST':
        if 'movement-form' in request.POST:
            form = MovementForm(request.POST)
            if form.is_valid():
                form.save()
                movement = form.instance.movement_name
                messages.success(request, f'{movement} movement created.')
                return redirect('staff_settings')
            else:
                errors = form.errors
                error_message = ''
                for field, error_list in errors.items():
                    error_message += f'{field}: {', '.join(error_list)}.'
                    messages.error(request, f'Failed to create movement. {error_message}.')

        elif 'list-form' in request.POST:
            form = ListForm(request.POST)
            if form.is_valid():
                form.save()
                list_name = form.instance.list_name
                messages.success(request, f'{list_name} list created.')
                return redirect('staff_settings')
            else:
                errors = form.errors
                error_message = ''
                for field, error_list in errors.items():
                    error_message += f'{field}: {', '.join(error_list)}.'
                    messages.error(request, f'Failed to create list. {error_message}.')

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
    return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def edit_movement(request, movement_id):
    cancel_url = request.META.get('HTTP_REFERER', '/')
    movement = get_object_or_404(WatchMovement, id=movement_id)
    associated = movement.watch_movement.count()
    if request.method == 'POST':
        form = MovementForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            messages.success(request, f'Changes saved.')
            return redirect('staff_settings')
        else:
            errors = form.errors
            error_message = ''
            for field, error_list in errors.items():
                error_message += f'{field}: {', '.join(error_list)}.'
            messages.error(request, f'Failed to edit movement. {error_message}.')
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
        return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def edit_list(request, list_id):
    cancel_url = request.META.get('HTTP_REFERER', '/')
    list_name = get_object_or_404(WatchList, id=list_id)
    associated = list_name.watch_list.count()
    if request.method == 'POST':
        form = ListForm(request.POST, instance=list_name)
        if form.is_valid():
            form.save()
            messages.success(request, f'Changes saved.')
            return redirect('staff_settings')
        else:
            errors = form.errors
            error_message = ''
            for field, error_list in errors.items():
                error_message += f'{field}: {', '.join(error_list)}.'
            messages.error(request, f'Failed to edit list. {error_message}.')
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
        return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def delete_movement(request, movement_id):
    movement = get_object_or_404(WatchMovement, id=movement_id)
    associated = movement.watch_movement.count()
    if request.method == 'POST':
        try:
            movement.delete()
            messages.success(request, f'{movement} movement deleted.')
            return redirect('staff_settings')
        except Exception as e:
            messages.error(request, f'Error occured while deleting movement: {str(e)}')
    else:
        movements = WatchMovement.objects.all()
        lists = WatchList.objects.values_list('list_name', flat=True)
        list_names = WatchList.objects.all()   
        context = {
            'associated': associated,
            'to_delete': movement,
            'movement_form': MovementForm(),
            'list_form': ListForm(),
            'movements': movements,
            'lists': lists,
            'list_names': list_names
        }
        return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def delete_list(request, list_id):
    list_name = get_object_or_404(WatchList, id=list_id)
    associated = list_name.watch_list.count()
    if request.method == 'POST':
        try:
            list_name.delete()
            messages.success(request, f'{list_name} deleted.')
            return redirect('staff_settings')
        except Exception as e:
            messages.error(request, f'Error occured while deleting: {str(e)}')
    else:
        movements = WatchMovement.objects.all()
        lists = WatchList.objects.values_list('list_name', flat=True)
        list_names = WatchList.objects.all()   
        context = {
            'associated': associated,
            'to_delete': list_name,
            'movement_form': MovementForm(),
            'list_form': ListForm(),
            'movements': movements,
            'lists': lists,
            'list_names': list_names
        }
        return render(request, 'watches/staff_settings.html', context)

@login_required(login_url='accounts/login')
def cancelProcess(request, content, cancel_url='home'):
    try:
        messages.info(request, f'{content} cancelled.')
        possible_lists = WatchList.objects.values_list('list_name', flat=True)
        if cancel_url in possible_lists:
            return redirect(reverse('watch_list', kwargs={'list_name': cancel_url}))
        return redirect(cancel_url)
    except Exception as e:
        messages.error(request, f'Error occured while cancelling: {str(e)}')
        return redirect('home')
