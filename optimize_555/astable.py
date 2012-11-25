from constants import ln2 #ln(2)

"""
Formulas describing the characteristics of a
555 timer in astable mode.

Default units:
R: ohms
C: F
period: s
freq: Hz

"""

def freq(r1, r2, c):
    """Compute the frequency of a 555 timer circuit
    in astable mode.

    :param r1: Resistor R1
    :param r2: Resistor R2
    :param c: Capacitor C
    :type r1: float (Ohms)
    :type r2: float (Ohms)
    :type c: float (farads)
    :return: return the oscillator frequency
    :type: float (hz)
    """
    return 1.0 / (ln2 * (float(r1) + 2.0 * r2) * float(c))

def period(r1, r2, c):
    """Compute the period of a 555 timer circuit
    in astable mode.

    :param r1: Resistor R1
    :param r2: Resistor R2
    :param c: Capacitor C
    :type r1: float (Ohms)
    :type r2: float (Ohms)
    :type c: float (farads)
    :return: return the oscillator period
    :type: float (seconds)
    """
    return ln2 * (float(r1) + (2.0 * r2)) * float(c)

def time_high(r1, r2, c):
    """Compute the length of time a 555 timer circuit
    in astable mode stays in activated or high.

    :param r1: Resistor R1
    :param r2: Resistor R2
    :param c: Capacitor C
    :type r1: float (Ohms)
    :type r2: float (Ohms)
    :type c: float (farads)
    :return: return the time the oscillator stays high
    :type: float (seconds)
    """
    return ln2 * (float(r1) + float(r2)) * float(c)

def time_low(r2, c):
    """Compute the length of time a 555 timer circuit
    in astable mode stays low.

    :param r2: Resistor R2
    :param c: Capacitor C
    :type r2: float (Ohms)
    :type c: float (farads)
    :return: return the time the oscillator stays low
    :type: float (seconds)
    """
    return ln2 * (float(r2) * float(c))

def duty( time_high, period ):
    """Compute the duty cycle of a 555 timer circuit's
    oscillation in astable mode.

    :param time_high: as computed by `time_high()`
    :param period: oscillator period as computed by `period()`
    :return: return the percentage active
    :type: float (%)
    """
    return time_high / period
