import dirac.complex as complex
import sys

HBAR = 1
hbar = complex.ToComplex(HBAR)
hbarSquared = hbar.square()
halfhbar = complex.ToComplex(.5 * HBAR)
ihbar = complex.i * hbar
isubhbar = complex.i / hbar

DELTA = .001 #sys.float_info.min
delta = complex.ToComplex(DELTA)