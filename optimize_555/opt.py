from scipy.optimize import brute
from astable import time_high, time_low, period
from defaults import R_set, C_set


def score(x, target_high, target_low, R_set, C_set):
    """scoring function for selecting from a set list
    of components"""
    R1_ix, R2_ix, C_ix = [int(round(xi)) for xi in x]

    R1 = R_set[R1_ix]
    R2 = R_set[R2_ix]
    C = C_set[C_ix]

    high = time_high(R1, R2, C)
    low = time_low(R2, C)

    high_d = abs(high - target_high)
    low_d = abs(low - target_low)

    # Tweak error function for desired optimization

    return high_d + low_d

def score_free(x, target_high, target_low):
    """scoring function for finding optimal
    component values within a defined range"""
    R1, R2, C = x

    high = time_high(R1, R2, C)
    low = time_low(R2, C)

    high_d = abs(high - target_high)
    low_d = abs(low - target_low)

    # Tweak error function to best fit requirements

    return high_d + low_d


def optimize(target_high, target_low, R_set=R_set, C_set=C_set):
    """Optimize for a set of available components
    :param target_high: Time that the oscillations should be high (secs).
    :param target_low: Time that the oscillations should be low (secs).
    :param R_set: Available resistor values
    :param C_set: Available capacitor values
    :type target_high: float (seconds)
    :type target_low: float (seconds)
    :type R_set: ordered list of floats (in Ohms)
    :type C_set: ordered list of floats (in Farads)
    :returns: values for R1, R2, and C; actual value for time_high and time_low
    :rtype: list of floats. [R1, R2, C, time_high, time_low]
    """
    # Calculate bounds
    MAX_R = len(R_set) - 1
    MAX_C = len(C_set) - 1

    lower = [0, 0, 0]
    upper = [MAX_R, MAX_R, MAX_C]

    # Optimize
    x_vals = brute(score, zip(lower, upper), 
            args=(target_high, target_low, R_set, C_set))

    r1_ix = int(round(x_vals[0]))
    r2_ix = int(round(x_vals[1]))
    c_ix = int(round(x_vals[2]))

    R1 = R_set[r1_ix]
    R2 = R_set[r2_ix]
    C = C_set[c_ix]

    th = time_high(R1, R2, C)
    tl = time_low(R2, C)

    return [R1, R2, C, th, tl]


def optimize_free(target_high, target_low, 
        R_range=(min(R_set), max(R_set)),
        C_range=(min(C_set), max(C_set))):
    """Optimize components given a range of allowable values.
    :param target_high: Time that the oscillations should be high (secs).
    :param target_low: Time that the oscillations should be low (secs).
    :param R_range: Bounds of allowable resistor values
    :param C_range: Bounds of allowable capacitor values
    :type target_high: float (seconds)
    :type target_low: float (seconds)
    :type R_range: tuple of floats. (min, max) (in Ohms)
    :type C_range: tuple of floats. (min, max) (in Farads)
    :returns: values for R1, R2, and C; actual value for time_high and time_low
    :rtype: list of floats. [R1, R2, C, time_high, time_low]
    """
    R1, R2, C = brute(score_free, [R_range, R_range, C_range], 
            args=(target_high, target_low),
            Ns= 50)
    th = time_high(R1, R2, C)
    tl = time_low(R2, C)

    return [R1, R2, C, th, tl]

HIGH_TARGET = 42.0
LOW_TARGET = 15 
optimize(HIGH_TARGET, LOW_TARGET)
optimize_free(HIGH_TARGET, LOW_TARGET)
