import math
import complex
import complexmatrix
from complexmatrix import CompexMatrix

HBAR = 1
hbar = complex.ToComplex(HBAR)
halfhbar = complex.ToComplex(.5 * HBAR)

pauliX = CompexMatrix([ [complex.zero, complex.one], [complex.one, complex.zero] ])
pauliY = CompexMatrix([ [complex.zero, complex.i], [-complex.i, complex.zero] ])
pauliZ = CompexMatrix([ [complex.one, complex.zero], [complex.zero, -complex.one] ])

spinX = pauliX.scale(halfhbar)
spinY = pauliY.scale(halfhbar)
spinZ = pauliZ.scale(halfhbar)

hadamard = CompexMatrix([ [complex.one, complex.one], [complex.one, -complex.one] ]).scale(complex.roothalf)

class WaveFunction:
    
    def totalProbability(self):
        
        """
        Get the total probability of the wave function.
        If it is not 1 then you should normilize it with
        the normalize() method.\n
        Example: < ψ | ψ > = 1
        """
        
        probability = 0
        
        for probabilityAmplitude in self.probabilityAmplitudes:
            probability += probabilityAmplitude.conjugateSquare()
            
        return probability
    
    def normalize(self):
        
        """
        Normilize the wave function.\n
        Example: \ ψ > => 1/√N \ ψ >
        """
        
        normalizationFactor = self.totalProbability()
        
        self.probabilityAmplitudes = list(map(lambda amplitude: complex.ToComplex(math.sqrt(1 / normalizationFactor)) * amplitude, self.probabilityAmplitudes))
            
        return self
    
    def __init__(self, probabilityAmplitudes=[], basis=[], **kwargs):
        
        """
        Initiate a wave function with given
        probability amplitudes and their state basis.\n
        Example: \ ψ > = Σ probability amplitude . \ state >
        """
        
        self.mass = kwargs.get('mass')
        
        if len(basis) == len(probabilityAmplitudes):
            
            self.basis = basis
            self.probabilityAmplitudes = probabilityAmplitudes
        
            self = self.normalize()
        
        else: raise AttributeError()
    
    def __str__(self):
        
        waveFunctionString = '[\n'
        
        for base, probabilityAmplitude in zip(self.basis, self.probabilityAmplitudes):
            
            waveFunctionString += f'\t{base}: {probabilityAmplitude}\n'
            
        waveFunctionString += ']'
        
        return waveFunctionString
    
    def __repr__(self): return f'Wave Function: {self.probabilityAmplitudes}'
    
    def __len__(self): return len(self.basis)
    
    def probabilityAmplitude(self, base):
        
        """
        Return the probability amplitude of a given state\n
        Example: probability amplitude =  < state | ψ >
        """
        
        index = self.basis.index(base)
        return self.probabilityAmplitudes[index]
    
    def probability(self, base):
        
        """
        Return the probability of a given state\n
        Example: probability =  < state | ψ >²
        """
        
        return self.probabilityAmplitude(base).conjugateSquare()
    
    def conjugate(self):
        
        """
        Conjugate wave function\n
        Example: < ψ / = \ ψ >*
        """
        
        self.probabilityAmplitudes = list(map(lambda probAmp: probAmp.conjugate(), self.probabilityAmplitudes))
        return self
    
    def probabilityDensity(self):
        
        """
        Convert wave function to probability density array.
        Example: probability density = ψ* ψ
        """
    
        return list(map(lambda probAmp: probAmp.conjugateSquare(), self.probabilityAmplitudes))
    
    def probabilityAmplitudeOfColapse(self, other):
        
        """
        Probability amplitude of wave function
        collapsing into another wave function\n
        Example: < ϕ | ψ >
        """
        
        if self.basis == other.basis:
            
            probability = complex.zero
            
            for base in self.basis:
                
                probability += other.probabilityAmplitude(base).conjugate() * self.probabilityAmplitude(base)
                
            return probability.real
        
        else: raise AttributeError() 
    
    def ket(self):
        
        """
        Return wave function as a ket.\n
        Example: \ ψ > = [ . . . ]
        """
        
        return CompexMatrix([self.probabilityAmplitudes])

    def bra(self):
        
        """
        Return wave function as a bra.\n
        Example: < ψ / = [ . . . ]
        """
        
        return[ [probabilityAmplitude.conjugate()] for probabilityAmplitude in self.probabilityAmplitudes ]

    def apply(self, operator):
        
        """
        Apply operator to the wave function.\n
        Example: \ ψ > => operator \ ψ >
        
        """
        
        probabilityAmplitudes = (operator @ self.ket()).matrix[0]
       
        return WaveFunction(probabilityAmplitudes, self.basis)
   
    def timeEvolve(self, potential, deltaX, deltaT):
        
        """
        Calculate how the wave function changes
        over small interval of time with a given
        potential. This returns
        the next wave function.\n
        Example: \ ψ > => [ 1 - i/ℏ H Δt ] \ ψ >
        
        """
        
        deltaX = complex.ToComplex(deltaX)
        deltaT = complex.ToComplex(deltaT)
        N = len(self)
        
        potential = list(map(lambda u:  complex.ToComplex(u), potential))
        
        laplaceOperator = complexmatrix.wideDiagonal(complex.ToComplex(-2), complex.one, (N, N))
        squaredMomentumOperator = laplaceOperator.scale(-hbar.square() / deltaX.square())
        hamiltonianOperator = squaredMomentumOperator.scale((complex.ToComplex(.5 / self.mass))) + complexmatrix.diagonal(potential, (N, N))
        timeEvolutionOperator = complexmatrix.identity((N, N)) - hamiltonianOperator.scale(complex.i * deltaT / hbar)
        
        result = self.apply(timeEvolutionOperator)
        return WaveFunction(result.probabilityAmplitudes, result.basis, mass=self.mass)