# calculating moonphase
from datetime import date


def moonphase():
    today = date.today()
    day_delta = (today - date(2000, 1, 6)).days
    synodic = 29.53058770576
    phase = day_delta % synodic

    match phase:
        case phase if 0 < phase <= 1.0:
            return 'new_moon'
        case phase if 1.0 < phase <= 6.382647:
            return 'waxing_crescent'
        case phase if 6.382647 < phase <= 8.382647:
            return 'first_quarter'
        case phase if 8.382647 < phase <= 13.765294:
            return 'waxing_gibbous'
        case phase if 13.765294 < phase <= 15.765294:
            return 'full_moon'
        case phase if 15.765294 < phase <= 21.147941:
            return 'waning_gibbous'
        case phase if 21.147941 < phase <= 23.147941:
            return 'last_quarter'
        case phase if 23.147941 < phase <= 28.530588:
            return 'waning_crescent'
        case phase if 28.530588 < phase <= 29.530588:
            return 'new_moon'
        case _:
            return 'moonphase'
