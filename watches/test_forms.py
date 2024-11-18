from django.test import TestCase
from .forms import WatchForm, MovementForm, ListForm
from .models import WatchList, WatchMovement


class TestWatchForm(TestCase):

    def setUp(self):
        """
        set up a list and movement instance for testing
        """
        self.test_list = WatchList.objects.create(list_name='test_list')
        self.test_movement = WatchMovement.objects.create(
            movement_name='test_movement'
        )

    def test_watch_make_is_required(self):
        """
        tests the make field is required by submitting the form with this
        field blank
        """
        form = WatchForm({
            'make': '',
            'movement_type': self.test_movement.id,
            'list_name': self.test_list.id
        })
        self.assertFalse(form.is_valid())
        self.assertIn('make', form.errors.keys())
        self.assertEqual(form.errors['make'][0], 'This field is required.')

    def test_watch_movement_type_is_required(self):
        """
        tests the movement_type field is required by submitting the form with this
        field blank
        """
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
        """
        tests the list_name field is required by submitting the form with this
        field blank
        """
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
        """
        submitting the form with just the required fields, all others
        are left empty
        """
        form = WatchForm({
            'make': 'test_make',
            'movement_type': self.test_movement.id,
            'list_name': self.test_list.id
        })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        testing the correct fields are shown in the form
        """
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
        """
        check that the input fields that aren't checkboxes have the
        correct classes assigned to them
        """
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
        """
        check that the complication checkboxes have the correct
        custom labels
        """
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
        """
        check that the complication checkboxes have the correct role, class
        and style assigned to them
        """
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
            self.assertEqual(form.fields[complication].widget.attrs, {
                'role': 'switch',
                'class': 'form-check-input',
                'style': 'height: 25px; width: 40px;'
            })

    def test_initial_list_if_provided(self):
        """
        test the list_name is prefilled if intital data is set
        """
        initial_data = {'list_name': self.test_list.id}
        form = WatchForm(initial=initial_data)
        self.assertEqual(form.fields['list_name'].initial, self.test_list.id)


class TestMovementForm(TestCase):

    def test_movement_is_required(self):
        """
        check the movement_name field is required by submitting the form
        with the field blank
        """
        form = MovementForm({'movement_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('movement_name', form.errors.keys())
        self.assertEqual(
            form.errors['movement_name'][0], 'This field is required.'
        )

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        check that movement_name is the only field in the form
        """
        form = MovementForm()
        self.assertEqual(form.Meta.fields, ['movement_name', ])

    def test_custom_label(self):
        """
        check the movment_name field custom name is correct
        """
        form = MovementForm()
        self.assertEqual(form.fields['movement_name'].label, '')

    def test_custom_widgets(self):
        """
        check the class, style and placeholder attributes are set correctly
        via widgets
        """
        form = MovementForm()
        self.assertEqual(
            form.fields['movement_name'].widget.attrs['style'], 'width: 100%;'
        )
        self.assertEqual(
            form.fields['movement_name'].widget.attrs['class'], 'form-control'
        )
        self.assertEqual(
            form.fields['movement_name'].widget.attrs['placeholder'],
            'enter new movement...'
        )

    def test_clean_movement_name_strips_whitespace(self):
        """
        test that entering data with leading and trailing whitespace
        is caught and cleaned correctly
        """
        form = MovementForm({'movement_name': '    Spring Drive   '})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['movement_name'], 'Spring Drive')

    def test_clean_movement_name_normalises_whitespace(self):
        """
        test that entering data with excess whitespace between words
        is caught and cleaned correctly
        """
        form = MovementForm({'movement_name': 'Spring       Drive'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['movement_name'], 'Spring Drive')

    def test_clean_movement_name_duplicate_case_insensitive(self):
        """
        test that case insensitive duplicate names are not accepted
        """
        self.test_movement = WatchMovement.objects.create(
            movement_name='test movement'
        )
        form = MovementForm({'movement_name': 'tEst movEmEnt'})
        self.assertFalse(form.is_valid())
        self.assertIn('movement_name', form.errors)
        self.assertEqual(
            form.errors['movement_name'][0],
            'A movement with this name already exists.'
        )

    def test_clean_movement_name_duplicate_with_extra_whitespace(self):
        """
        test that duplicate names with leading, trailing and excess whitespace
        between words are not accepted
        """
        self.test_movement = WatchMovement.objects.create(
            movement_name='test movement'
        )
        form = MovementForm({'movement_name': '  Test     moveMent  '})
        self.assertFalse(form.is_valid())
        self.assertIn('movement_name', form.errors)
        self.assertEqual(
            form.errors['movement_name'][0],
            'A movement with this name already exists.'
        )

    def test_valid_entry(self):
        """
        testing a valid entry is accepted
        """
        form = MovementForm({'movement_name': 'Perpetual Motion'})
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data['movement_name'], 'Perpetual Motion'
        )


class TestListForm(TestCase):

    def test_list_name_is_required(self):
        """
        check the friendly_name field is required by submitting the form
        with the field blank
        """
        form = ListForm({'friendly_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('friendly_name', form.errors.keys())
        self.assertEqual(
            form.errors['friendly_name'][0], 'This field is required.'
        )

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        check that friendly_name is the only field in the form
        """
        form = ListForm()
        self.assertEqual(form.Meta.fields, ['friendly_name', ])

    def test_custom_label(self):
        """
        check the friendly_name field custom name is correct
        """
        form = ListForm()
        self.assertEqual(form.fields['friendly_name'].label, '')

    def test_custom_widgets(self):
        """
        check the class, style and placeholder attributes are set correctly
        via widgets
        """
        form = ListForm()
        self.assertEqual(
            form.fields['friendly_name'].widget.attrs['style'], 'width: 100%;'
        )
        self.assertEqual(
            form.fields['friendly_name'].widget.attrs['class'], 'form-control'
        )
        self.assertEqual(
            form.fields['friendly_name'].widget.attrs['placeholder'],
            'enter new list...'
        )

    def test_clean_movement_name_strips_whitespace(self):
        """
        test that entering data with leading and trailing whitespace
        is caught and cleaned correctly
        """
        form = ListForm({'friendly_name': '    Wish List   '})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['friendly_name'], 'Wish List')

    def test_clean_movement_name_normalises_whitespace(self):
        """
        test that entering data with excess whitespace between words
        is caught and cleaned correctly
        """
        form = ListForm({'friendly_name': 'Wish       List'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['friendly_name'], 'Wish List')

    def test_clean_movement_name_duplicate_case_insensitive(self):
        """
        test that case insensitive duplicate names are not accepted
        """
        self.test_list = WatchList.objects.create(
            friendly_name='test list'
        )
        form = ListForm({'friendly_name': 'tEst lIsT'})
        self.assertFalse(form.is_valid())
        self.assertIn('friendly_name', form.errors)
        self.assertEqual(
            form.errors['friendly_name'][0],
            'A list with this name already exists.'
        )

    def test_clean_movement_name_duplicate_with_extra_whitespace(self):
        """
        test that duplicate names with leading, trailing and excess whitespace
        between words are not accepted
        """
        self.test_list = WatchList.objects.create(
            friendly_name='test list'
        )
        form = ListForm({'friendly_name': '  Test     lISt  '})
        self.assertFalse(form.is_valid())
        self.assertIn('friendly_name', form.errors)
        self.assertEqual(
            form.errors['friendly_name'][0],
            'A list with this name already exists.'
        )

    def test_valid_entry(self):
        """
        testing a valid entry is accepted
        """
        form = ListForm({'friendly_name': 'Gift List'})
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data['friendly_name'], 'Gift List'
        )
