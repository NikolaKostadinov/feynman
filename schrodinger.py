import math
import complex
from complex import Complex
import complexmatrix
from complexmatrix import CompexMatrix
import quantum
from quantum import WaveFunction

from matplotlib import pyplot, animation

NUMBER_OF_X = 100
NUMBER_OF_T = 100

START = -1
END = 1

TOTAL_TIME = .01

MASS = 1

length = abs(END - START)

deltaX = length / NUMBER_OF_X
deltaT = TOTAL_TIME / NUMBER_OF_T

X = [ x * deltaX + START for x in range(NUMBER_OF_X) ]

INIT_WAVE_FUNCTION = lambda x: math.sin(100*math.pi * x)
initialWaveFunction = WaveFunction([ complex.ToComplex(INIT_WAVE_FUNCTION(x)) for x in X ], X, mass=MASS)

POTENTIAL = lambda x: 0
potential = [ POTENTIAL(x) for x in X ]

fullWaveFunction = [ WaveFunction() for _ in range(NUMBER_OF_T) ]
fullWaveFunction[0] = initialWaveFunction

# Schrodinger Equation

for t in range(len(fullWaveFunction) - 1):
    
    fullWaveFunction[t + 1] = fullWaveFunction[t].timeEvolve(potential, deltaX, deltaT)
    
probabilityDensity = fullWaveFunction[-1].probabilityDensity()

# Animation

fig = pyplot.figure()
ax = pyplot.axes(xlim=(START, END), ylim=(0, .75))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(t):
    line.set_data(X, fullWaveFunction[t-1].probabilityDensity())
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=NUMBER_OF_T, interval=40, blit=True)
pyplot.show()