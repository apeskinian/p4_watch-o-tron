from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Watch, WatchList, WatchMovement
from .forms import WatchForm, MovementForm, ListForm
import datetime


@login_required(login_url='accounts/login')
def home(request, list_name='collection'):
    """
    Displays a users watches in the requested list :model:`watches.Watch` and
    retrieves the available lists :model:`watches.WatchList`.
    **Arguments**
    ``list_name`` (str, optional):
        The url path argument of the list that the user wishes to view.
    **Context**
    ``day``
        The current day as an integer (range 0-6)
        Used for setting complication icons.
    ``date``
        The current date as an integer (range 1-31)
        Used for setting complication icons.
    ``watches``
        A queryset of watch objects filtered by user and chosen list type.
    ``lists``
        A queryset of all the lists.
    ``current_list``
        Name of the currently viewed list (from the `list_name` field, string).
    **Template:**
    :template:`watches/home.html`
    """
    lists = WatchList.objects.all()
    watches = Watch.objects.filter(
        owner=request.user,
        list_name__list_name=list_name
    ).order_by('make', 'collection', 'model')
    current_list = get_object_or_404(WatchList, list_name=list_name)
    day = datetime.datetime.now()
    context = {
        'day': day.strftime('%w'),
        'date': day.strftime('%d'),
        'watches': watches,
        'lists': lists,
        'current_list': current_list.list_name
    }
    messages.success(request, f'Switched to {current_list.friendly_name}')
    return render(request, 'watches/home.html', context)


@login_required(login_url='accounts/login')
def manage_watch(request, origin, watch_id=None):
    """
    Adds or edits an instance of :model:`watches.Watch` specified by the user.
    **Arguments**
    ``origin`` (str):
        The url name of the list that the action was called from.
    ``watch_id`` (int, optional):
        The primary key of the watch object to be edited.
    **Context**
    ``day``
        The current day as an integer (range 0-6)
        Used for setting complication icons.
    ``date``
        The current date as an integer (range 1-31)
        Used for setting complication icons.
    ``origin``
        Name of the list that the user was viewing when the action was called.
    **Conditional Context**
    ``watch_form``
        An instance of :form:`watches.WatchForm`. If adding this form will
        be empty. If editing it will be prefilled with data from an
        instance of :model:`watches.Watch`
    ``watch``
        An instance of :model:`watches.Watch` which is included if editing.
    ``mode``
        Used to control template logic according to whether the user is
        adding a new watch or editing an existing watch.
    **Template:**
    :template:`watches/manage_watch.html`
    """
    if request.method == 'POST':
        # check if a watch object was sent with request and create form
        # accordingly
        if watch_id:
            watch = get_object_or_404(Watch, id=watch_id)
            form = WatchForm(request.POST, request.FILES, instance=watch)
        else:
            form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            new_list = form.instance.list_name
            # send the correct message based on whether a watch object was
            # sent in the request as a parameter
            if watch_id:
                messages.success(
                    request,
                    f'{watch.make} watch editted successfully'
                )
            else:
                messages.success(
                    request,
                    f'Added {form.instance.make} watch '
                    f'to {new_list.friendly_name}'
                )
            return redirect('watch_list', list_name=new_list.list_name)
        else:
            errors = form.errors
            error_message = ''
            for field, error_list in errors.items():
                error_message += f'{field}: {', '.join(error_list)}.'
            messages.error(request, f'An error occured. {error_message}.')
    else:
        day = datetime.datetime.now()
        context = {
            'day': day.strftime('%w'),
            'date': day.strftime('%d'),
            "origin": origin,
            "watch_form": WatchForm(),
            "mode": 'add',
        }
        if watch_id:
            watch = get_object_or_404(Watch, id=watch_id)
            context.update({
                "watch_form": WatchForm(instance=watch),
                "watch": watch,
                "mode": 'edit',
            })
        return render(request, 'watches/manage_watch.html', context)


@login_required(login_url='accounts/login')
def purchase_watch(request, watch_id):
    """
    Moves an instance of :model:`watches`Watch to the users collection from
    their wish list.
    **Arguments**
    ``watch_id`` (int):
        The primary key of the watch object to be edited.
    **Context**
    ``watch_list``
        The URL name to redirect to.
    ``collection``
        The argument for the URL requesting to show the collection list.
    """
    try:
        watch = get_object_or_404(Watch, id=watch_id)
        collection_list = get_object_or_404(WatchList, list_name='collection')
        watch.list_name = collection_list
        messages.success(request, f'{watch.make} watch moved to Collection')
        watch.save()
    except Exception as e:
        messages.error(
            request,
            f'Error occured while moving watch to Collection: {str(e)}'
        )
    return redirect('watch_list', 'collection')


@login_required(login_url='accounts/login')
def delete_watch(request, watch_id):
    """
    Deletes an instance of :model:`watches`Watch from a users list.
    **Arguments**
    ``watch_id`` (int):
        The primary key of the watch object to be deleted.
    **Context**
    ``return_url``
        The URL path to redirect to, the referring page.
    """
    try:
        return_url = request.META.get('HTTP_REFERER', '/')
        watch = get_object_or_404(Watch, id=watch_id)
        messages.info(
            request,
            f'{watch.make} watch deleted from {watch.list_name}'
        )
        watch.delete()
    except Exception as e:
        messages.error(
            request,
            f'Error occured while deleting watch: {str(e)}'
        )
    return redirect(return_url)


def get_staff_settings_context():
    """Returns the shared context for staff settings views.
    **Returns**
    ``movement_form``
        An instance of :form:`watches.MovementForm`.
    ``list_form``
        An instance of :form:`watches.ListForm`.
    ``movements``
        A queryset of all current movement objects.
    ``list_names``
        A queryset of all current list objects.
    """
    return {
        'movement_form': MovementForm(),
        'list_form': ListForm(),
        'movements': WatchMovement.objects.all(),
        'list_names': WatchList.objects.all()
    }


@staff_member_required(login_url='accounts/login')
def staff_settings(request):
    """
    Shows staff members a list of movement types from
    :model:`watches.WatchMovement` and list options from
    :model:`Watches.WatchList`. Also allows creation of new instances.
    **Context**
    Shared context is retrieved from `def get_staff_settings_context():`.
    **Template:**
    :template:`watches/staff_settings.html`
    """
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
                    for error in error_list:
                        error_message += f'{error}\n'
                messages.error(request, error_message)
        elif 'list-form' in request.POST:
            form = ListForm(request.POST)
            if form.is_valid():
                form.save()
                list_name = form.instance.friendly_name
                messages.success(request, f'{list_name} created.')
                return redirect('staff_settings')
            else:
                errors = form.errors
                error_message = ''
                for field, error_list in errors.items():
                    for error in error_list:
                        error_message += f'{error}\n'
                messages.error(request, error_message)

    context = get_staff_settings_context()
    return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def edit_movement(request, movement_id):
    """
    Edits a chosen movement and lets the staff member know how many related
    watch objects will be affected by the change.
    **Arguments**
    ``movement_id`` (int):
        The primary key of the movement object to be edited.
    **Context**
        Shared context is retrieved from `def get_staff_settings_context():`.
    **Additional Context**
    ``associated``
        The number of watch objects that are related to this movement.
    ``edit_form``
        An instance of :form:`Watches.MovementForm` prefilled with movement
        to edit.
    **Template:**
    :template:`watches/staff_settings.html`
    """
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
                error_message += f'{field}: {', '.join(error_list)}'
            messages.error(
                request,
                f'Failed to edit movement. {error_message}'
            )
            return redirect('staff_settings')
    else:
        context = get_staff_settings_context()
        context.update({
            'associated': associated,
            'edit_form': MovementForm(instance=movement)
        })
        return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def edit_list(request, list_id):
    """
    Edits a chosen movement and lets the staff member know how many related
    watch objects will be affected by the change.
    **Arguments**
    ``list_id`` (int):
        The primary key of the list object to be edited.
    **Context**
        Shared context is retrieved from `def get_staff_settings_context():`.
    **Additional Context**
    ``associated``
        The number of watch objects that are related to this movement.
    ``edit_form``
        An instance of :form:`Watches.MovementForm` prefilled with movement
        to edit.
    **Template:**
    :template:`watches/staff_settings.html`
    """
    list_name = get_object_or_404(WatchList, id=list_id)
    associated = list_name.watch_list.count()

    if request.method == 'POST':
        form = ListForm(request.POST, instance=list_name)
        if form.is_valid():
            form.save()
            messages.success(request, f'Changes saved')
            return redirect('staff_settings')
        else:
            errors = form.errors
            error_message = ''
            for field, error_list in errors.items():
                error_message += f'{field}: {', '.join(error_list)}.'
            messages.error(request, f'Failed to edit list. {error_message}')
            return redirect('staff_settings')
    else:
        context = get_staff_settings_context()
        context.update({
            'associated': associated,
            'edit_form': ListForm(instance=list_name)
        })
        return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def delete_movement(request, movement_id):
    """
    Deletes a chosen movement and lets the staff member know how many related
    watch objects will be affected by the change.
    **Arguments**
    ``movement_id`` (int):
        The primary key of the movement object to be deleted.
    **Context**
        Shared context is retrieved from `def get_staff_settings_context():`.
    **Additional Context**
    ``associated``
        The number of watch objects that are related to this movement.
    ``to_delete``
        An instance of :model:`Watches.WatchMovement`.
    **Template:**
    :template:`watches/staff_settings.html`
    """
    movement = get_object_or_404(WatchMovement, id=movement_id)
    associated = movement.watch_movement.count()

    if request.method == 'POST':
        try:
            movement.delete()
            messages.success(request, f'{movement} movement deleted')
            return redirect('staff_settings')
        except Exception as e:
            messages.error(
                request,
                f'Error occured while deleting movement: {str(e)}'
            )
            return redirect('staff_settings')
    else:
        context = get_staff_settings_context()
        context.update({
            'associated': associated,
            'to_delete': movement
        })
        return render(request, 'watches/staff_settings.html', context)


@staff_member_required(login_url='accounts/login')
def delete_list(request, list_id):
    """
    Deletes a chosen list and lets the staff member know how many related
    watch objects will be affected by the change.
    **Arguments**
    ``list_id`` (int):
        The primary key of the list object to be deleted.
    **Context**
        Shared context is retrieved from `def get_staff_settings_context():`.
    **Additional Context**
    ``associated``
        The number of watch objects that are related to this movement.
    ``to_delete``
        An instance of :model:`Watches.WatchList`.
    **Template:**
    :template:`watches/staff_settings.html`
    """
    list_name = get_object_or_404(WatchList, id=list_id)
    associated = list_name.watch_list.count()

    if request.method == 'POST':
        try:
            list_name.delete()
            messages.success(request, f'{list_name} deleted')
            return redirect('staff_settings')
        except Exception as e:
            messages.error(request, f'Error occured while deleting: {str(e)}')
            return redirect('staff_settings')
    else:
        context = get_staff_settings_context()
        context.update({
            'associated': associated,
            'to_delete': list_name
        })
        return render(request, 'watches/staff_settings.html', context)


@login_required(login_url='accounts/login')
def cancel_process(request, content, cancel_url='home'):
    """
    Called when an action is cancelled by the user.
    **Arguments**
    ``content`` (str):
        Information regarding what action is being cancelled, this is used
        in the provided messsage.
    ``cancel_url`` (str, optional):
        The url name that the action was taken from.
    **Context**
    ``cancel_url``
        If an instance with 'list_name' matching 'cancel_url' is in
        :model:`watches.WatchList`, the user is redirected to that list.
    ``home``
        If no matches are found user is redirected to 'home'.
    """
    try:
        messages.info(request, f'{content} cancelled.')
        possible_lists = WatchList.objects.values_list('list_name', flat=True)
        if cancel_url in possible_lists:
            return redirect(
                reverse(
                    'watch_list',
                    kwargs={'list_name': cancel_url})
            )
        return redirect(cancel_url)
    except Exception as e:
        messages.error(request, f'Error occured while cancelling: {str(e)}')
        return redirect('home')
