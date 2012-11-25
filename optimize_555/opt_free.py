from scipy.optimize import brute
from astable import time_high, time_low, period


R_range = [100, 10e6]
C_range = [1e-12, 1000e-6]

HIGH_TARGET = 42.0
LOW_TARGET = 15

def score(x):
    R1,R2,C = x

    high = time_high(R1, R2, C)
    low = time_low(R2, C)

    high_d = abs(high - HIGH_TARGET)
    low_d = abs(low - LOW_TARGET)

    # Tweak error function to best fit requirements

    return high_d + low_d

results = brute(score, [R_range, R_range, C_range], Ns= 50)

print "Final"
R1, R2, C = results
print "R1: %.3e Ohms" % R1
print "R2: %.3e Ohms" % R2
print "C: %.3e F" % C

print "Time High: %.3f" % time_high(R1, R2, C)
print "Time Low: %.3f" % time_low(R2, C)





