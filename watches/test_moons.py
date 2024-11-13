from django.test import TestCase
from unittest.mock import patch
from datetime import date, datetime
from .utils.moons import moonphase

class TestMoonPhases(TestCase):

    def test_new_moon(self):
        known_new_moon = date(2024, 11, 1)
        self.assertEqual(moonphase(known_new_moon), 'new_moon')

    def test_waxing_crescent(self):
        known_waxing_crescent = date(2024, 11, 3)
        self.assertEqual(moonphase(known_waxing_crescent), 'waxing_crescent')

    def test_first_quarter(self):
        known_first_quarter = date(2024, 11, 9)
        self.assertEqual(moonphase(known_first_quarter), 'first_quarter')

    def test_waxing_gibbous(self):
        known_waxing_gibbous = date(2024, 11, 12)
        self.assertEqual(moonphase(known_waxing_gibbous), 'waxing_gibbous')

    def test_full_moon(self):
        known_full_moon = date(2024, 11, 16)
        self.assertEqual(moonphase(known_full_moon), 'full_moon')

    def test_waning_gibbous(self):
        known_waning_gibbous = date(2024, 11, 18)
        self.assertEqual(moonphase(known_waning_gibbous), 'waning_gibbous')

    def test_last_quarter(self):
        known_last_quarter = date(2024, 11, 23)
        self.assertEqual(moonphase(known_last_quarter), 'last_quarter')

    def test_waning_crescent(self):
        known_waning_crescent = date(2024, 11, 26)
        self.assertEqual(moonphase(known_waning_crescent), 'waning_crescent')
    
    def test_new_moon_again(self):
        known_waning_crescent = date(2024, 10, 31)
        self.assertEqual(moonphase(known_waning_crescent), 'new_moon')

    @patch('ephem.previous_new_moon')
    def test_moonphase_fallback_case(self, mock_previous_new_moon):
        # override previous new moon date to today so delta is 0
        mock_return = mock_previous_new_moon.return_value
        mock_return.datetime.return_value.date.return_value = date.today()
        result = moonphase()
        self.assertEqual(result, 'new_moon')
