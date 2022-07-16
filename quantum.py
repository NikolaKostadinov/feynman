import math
import complex
from complex import Complex
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
            
            if isinstance(probabilityAmplitude, Complex):
                probability += probabilityAmplitude.conjugateSquare()
            elif isinstance(probabilityAmplitude, WaveFunction):
                probability += probabilityAmplitude.totalProbability()
            else: TypeError()
            
        return probability
    
    def scale(self, factor: Complex):
        
        """
        Scale every probability amplitude by some factor.\n
        Example: \ ψ > => f . \ ψ >
        """
        
        def scaleAmplitude(probabilityAmplitude):
            
            if isinstance(probabilityAmplitude, Complex):
                return probabilityAmplitude * factor
            elif isinstance(probabilityAmplitude, WaveFunction):
                return probabilityAmplitude.scale(factor)
            else: TypeError()
        
        self.probabilityAmplitudes = [ scaleAmplitude(probabilityAmplitude) for probabilityAmplitude in self.probabilityAmplitudes ]
        
        return self
    
    def normalize(self, normalizeTo: float = 1):
        
        """
        Normilize the wave function.\n
        Example: \ ψ > => 1/√N \ ψ >
        """
        
        normalizationFactor = complex.ToComplex(math.sqrt(normalizeTo / self.totalProbability())) 

        self = self.scale(normalizationFactor)
            
        return self
    
    def __init__(self, probabilityAmplitudes: list = [], basis: list = []):
        
        """
        Initiate a wave function with given
        probability amplitudes and their state basis.\n
        Example: \ ψ > = Σ probability amplitude . \ state >
        """
        
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
        
        probabilityAmplitude = self.probabilityAmplitude(base)
        
        if isinstance(probabilityAmplitude, Complex):
            return probabilityAmplitude.conjugateSquare()
        elif isinstance(probabilityAmplitude, WaveFunction):
            return probabilityAmplitude.totalProbability()
        else: TypeError()
    
    def conjugate(self):
        
        """
        Conjugate wave function\n
        Example: < ψ / = \ ψ >*
        """
        
        self.probabilityAmplitudes = [ probabilityAmplitude.conjugate() for probabilityAmplitude in self.probabilityAmplitudes ]
        
        return self
    
    def probabilityDensity(self):
        
        """
        Convert wave function to probability density array.
        Example: probability density = ψ* ψ
        """
    
        def probabilityDensityOfAmplitude(probabilityAmplitude):
            
            if isinstance(probabilityAmplitude, Complex):
                return probabilityAmplitude.conjugateSquare()
            elif isinstance(probabilityAmplitude, WaveFunction):
                return probabilityAmplitude.probabilityDensity()
            else: TypeError()
        
        return [ probabilityDensityOfAmplitude(probabilityAmplitude) for probabilityAmplitude in self.probabilityAmplitudes ]
    
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
        Example: < ψ / = [ ' ' ' ]
        """
        
        return [ [probabilityAmplitude.conjugate()] for probabilityAmplitude in self.probabilityAmplitudes ]

    def apply(self, operator: CompexMatrix):
        
        """
        Apply operator to the wave function.\n
        Example: \ ψ > => operator \ ψ >
        
        """
        
        probabilityAmplitudes = (operator @ self.ket()).matrix[0]
       
        return WaveFunction(probabilityAmplitudes, self.basis)
   
    def timeEvolve(self, hamiltonian: CompexMatrix):
        
        """
        Calculate how the wave function changes
        over small interval of time with a given
        potential. This returns
        the next wave function.\n
        Example: \ ψ > => [ 1 - i/ℏ H Δt ] \ ψ >
        
        """
        
        DELTA_T = .0000001
        deltaT = complex.ToComplex(DELTA_T)
        N = len(self)
        
        timeEvolutionOperator = complexmatrix.identity((N, N)) - hamiltonian.scale(complex.i * deltaT / hbar)
        
        result = self.apply(timeEvolutionOperator)
        return WaveFunction(result.probabilityAmplitudes, result.basis, mass=self.mass)