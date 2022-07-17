import dirac.complex as complex
import sys

HBAR = 1
hbar = complex.ToComplex(HBAR)
halfhbar = complex.ToComplex(.5 * HBAR)
ihbar = complex.i * hbar
isubhbar = complex.i / hbar

DELTA = sys.float_info.min
delta = complex.ToComplex(DELTA)