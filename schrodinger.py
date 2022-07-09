import math
import complex
from complex import Complex
import complexmatrix
from complexmatrix import CompexMatrix
import quantum
from quantum import WaveFunction

from matplotlib import pyplot

NUMBER_OF_X = 100
NUMBER_OF_T = 100

START = -1
END = 1

TOTAL_TIME = 10

MASS = 1

length = abs(END - START)

deltaX = length / NUMBER_OF_X
deltaT = TOTAL_TIME / NUMBER_OF_T

X = [ x * deltaX + START for x in range(NUMBER_OF_X) ]

INIT_WAVE_FUNCTION = lambda x: complex.ToComplex(math.cos(x))
initialWaveFunction = WaveFunction([ INIT_WAVE_FUNCTION(x) for x in X ], X, mass=MASS)

POTENTIAL = lambda x: 0
potential = [ POTENTIAL(x) for x in X ]

fullWaveFunction = [ None for _ in range(NUMBER_OF_T) ]
fullWaveFunction[0] = initialWaveFunction

for t in range(len(fullWaveFunction) - 1):
    
    fullWaveFunction[t + 1] = fullWaveFunction[t].timeEvolve(potential)
    
probabilityDensity = fullWaveFunction[-1].probabilityDensity()

pyplot.plot(X, probabilityDensity, color='g')
pyplot.show()