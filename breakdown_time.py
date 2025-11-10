# 3) breakdown_time(seconds)
#    Convert a non-negative integer number of seconds into as few units as
#    possible using 3600, 60, and 1. Return a dictionary like {3600: h, 60: m, 1: s}.
#    If input is invalid (not int or negative), return -1.
#    For seconds == 0, return {}.


def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    elif seconds == 0:
        return {}

    pattern = [3600, 60, 1]
    formatted = {}
    for unit in pattern:
        secondsByUnit = seconds // unit
        if secondsByUnit == 0:
            break
        formatted[unit] = secondsByUnit
        seconds = seconds % unit

    return formatted
