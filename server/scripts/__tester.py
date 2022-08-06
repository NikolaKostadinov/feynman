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
T = 200
basis = [ (x - N/2) / 1000 for x in range(N) ]
waveFunction = [ complex.ToComplex(math.cos(math.pi * x / N)) for x in basis ]
PSI = QuantumState(waveFunction, basis)

waveFunction = [ PSI ]
potential = [ -1000000 for x in basis ]
potential[N//3:N//2] = [ 10000000 for _ in range(N//3, N//2) ]
for _ in range(T):
    waveFunction.append(waveFunction[-1].shrodingerEvolve(.0001, potential))

fig = pyplot.figure()
ax = pyplot.axes(xlim=(basis[0], basis[-1]), ylim=(0, 1))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(t):
    line.set_data(basis, waveFunction[t-1].probabilityDensity())
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=T, interval=50, blit=True)
pyplot.show()