from django.test import TestCase
from .forms import WatchForm, MovementForm, ListForm
from .models import WatchList, WatchMovement


class TestWatchForm(TestCase):

    def setUp(self):
        # setting up test movement and list options
        self.test_list = WatchList.objects.create(list_name='test_list')
        self.test_movement = WatchMovement.objects.create(
            movement_name='test_movement'
        )

    def test_watch_make_is_required(self):
        form = WatchForm({
            'make': '',
            'movement_type': self.test_movement.id,
            'list_name': self.test_list.id
        })
        self.assertFalse(form.is_valid())
        self.assertIn('make', form.errors.keys())
        self.assertEqual(form.errors['make'][0], 'This field is required.')
    
    def test_watch_movement_type_is_required(self):
        form = WatchForm({
            'make': 'test_make',
            'movement_type': '',
            'list_name': self.test_list.id
        })
        self.assertFalse(form.is_valid())
        self.assertIn('movement_type', form.errors.keys())
        self.assertEqual(
            form.errors['movement_type'][0], 'This field is required.'
        )
    
    def test_watch_list_name_required(self):
        form = WatchForm({
            'make': 'test_make',
            'movement_type': self.test_movement.id,
            'list_name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('list_name', form.errors.keys())
        self.assertEqual(
            form.errors['list_name'][0], 'This field is required.'
        )

    def test_all_other_fields_are_optional(self):
        form = WatchForm({
            'make': 'test_make',
            'movement_type': self.test_movement.id,
            'list_name': self.test_list.id
        })
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        form = WatchForm()
        self.assertEqual(form.Meta.fields, [
            'make',
            'collection',
            'model',
            'movement_type',
            'movement_model',
            'complication_chronograph',
            'complication_date',
            'complication_day',
            'complication_gmt',
            'complication_world_timer',
            'complication_moonphase',
            'complication_power_reserve',
            'complication_tourbillon',
            'image',
            'list_name',
        ])

    def test_non_complication_widgets(self):
        form = WatchForm()
        for formField in [
            'make',
            'collection',
            'model',
            'movement_type',
            'movement_model',
            'image',
            'list_name',
        ]:
            self.assertEqual(
                form.fields[formField].widget.attrs['class'], 'form-control'
            )
            self.assertEqual(
                form.fields[formField].widget.attrs['style'], 'width: 100%;'
            )


    def test_complication_custom_labels(self):
        form = WatchForm()
        self.assertEqual(
            form.fields['complication_chronograph'].label, 'Chronograph'
        )
        self.assertEqual(form.fields['complication_date'].label, 'Date')
        self.assertEqual(form.fields['complication_day'].label, 'Day')
        self.assertEqual(form.fields['complication_gmt'].label, 'GMT')
        self.assertEqual(
            form.fields['complication_world_timer'].label, 'World Timer'
        )
        self.assertEqual(
            form.fields['complication_moonphase'].label, 'Moonphase'
        )
        self.assertEqual(
            form.fields['complication_power_reserve'].label, 'Power Reserve'
        )
        self.assertEqual(
            form.fields['complication_tourbillon'].label, 'Tourbillon'
        )

    def test_complication_custom_widgets(self):
        form = WatchForm()
        for complication in [
            'complication_chronograph',
            'complication_date',
            'complication_day',
            'complication_gmt',
            'complication_world_timer',
            'complication_moonphase',
            'complication_power_reserve',
            'complication_tourbillon',
        ]:
            self.assertEqual(form.fields[complication].widget.attrs,
                {
                    'role': 'switch',
                    'class': 'form-check-input',
                    'style': 'height: 25px; width: 40px;'
                }
        )


class TestMovementForm(TestCase):

    def test_movement_is_required(self):
        form = MovementForm({'movement_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('movement_name', form.errors.keys())
        self.assertEqual(
            form.errors['movement_name'][0], 'This field is required.'
        )

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MovementForm()
        self.assertEqual(form.Meta.fields, ['movement_name',])


class TestListForm(TestCase):

    def test_list_name_is_required(self):
        form = ListForm({'friendly_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('friendly_name', form.errors.keys())
        self.assertEqual(
            form.errors['friendly_name'][0], 'This field is required.'
        )

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ListForm()
        self.assertEqual(form.Meta.fields, ['friendly_name',])
