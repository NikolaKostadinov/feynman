import math
import dirac.complex as complex
from dirac.complex import Complex
import dirac.complexmatrix as complexmatrix
from dirac.complexmatrix import ComplexMatrix
import dirac.operator as operator
from dirac.operator import Operator
import dirac.state as state
from dirac.state import QuantumState
from matplotlib import pyplot, animation

N = 100
T = 100

L = 10
n = 10
mass = 1
initialFunction = lambda x: math.sin(n * math.pi * x / L)
potentialFunction = lambda x: 0

X = [ index * L / N for index in range(N) ]

potentialField = [ potentialFunction(x) for x in X ]

initialWave = [ complex.ToComplex(initialFunction(x)) for x in X ]
initialState = QuantumState(initialWave, X)

PSI = [initialState]
for t in range(1, T): PSI.append(PSI[-1].shrodingerEvolve(mass, potentialField))

fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, L), ylim=(0, 1))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(t):
    line.set_data(X, PSI[t-1].probabilityDensity())
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=T, interval=50, blit=True)
pyplot.show()