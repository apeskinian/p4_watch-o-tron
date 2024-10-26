# calculating moonphase
import ephem
from datetime import date


def moonphase():
    # Get today's date
    today = date.today()

    # Set up the observer
    moon = ephem.Moon()
    moon.compute(today.strftime("%Y/%m/%d"))

    # The moon phase angle: 0 = new moon, 180 = full moon
    phase_angle = moon.phase

    # Determine the moon phase based on the angle
    if 0 <= phase_angle < 1:
        return 'new_moon'
    elif 1 <= phase_angle < 90:
        return 'waxing_crescent'
    elif 90 <= phase_angle < 100:
        return 'first_quarter'
    elif 100 <= phase_angle < 170:
        return 'waxing_gibbous'
    elif 170 <= phase_angle <= 180:
        return 'full_moon'
    elif 180 < phase_angle <= 260:
        return 'waning_gibbous'
    elif 260 < phase_angle < 270:
        return 'last_quarter'
    elif 270 <= phase_angle < 360:
        return 'waning_crescent'
    else:
        return 'new_moon'
