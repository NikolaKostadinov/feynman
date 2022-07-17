import math
import dirac.complex as complex
from dirac.complex import Complex
import dirac.complexmatrix as complexmatrix
from dirac.complexmatrix import CompexMatrix
import dirac.constants as constants
import dirac.operator as operator
from dirac.operator import Operator

class QuantumState:
    
    def totalProbability(self):
        
        """
        Get the total probability of the state.
        If it is not 1 then you should normilize it with
        the normalize() method.\n
        Example: < ψ | ψ > = 1
        """
        
        probability = 0
        
        for probabilityAmplitude in self.probabilityAmplitudes:
            
            if isinstance(probabilityAmplitude, Complex):
                probability += probabilityAmplitude.conjugateSquare()
            elif isinstance(probabilityAmplitude, QuantumState):
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
            elif isinstance(probabilityAmplitude, QuantumState):
                return probabilityAmplitude.scale(factor)
            else: TypeError()
        
        self.probabilityAmplitudes = [ scaleAmplitude(probabilityAmplitude) for probabilityAmplitude in self.probabilityAmplitudes ]
        
        return self
    
    def normalize(self, normalizeTo: float = 1):
        
        """
        Normilize the quantum state. You can also
        normilize it so it has an arbitrary total probability.\n
        Example: \ ψ > => 1/√N \ ψ >
        """
        
        normalizationFactor = complex.ToComplex(math.sqrt(normalizeTo / self.totalProbability())) 

        self = self.scale(normalizationFactor)
            
        return self
    
    def __init__(self, probabilityAmplitudes: list = [], basis: list = []):
        
        """
        Initiate a quantum state with given
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
        Return the probability amplitude of a given state.\n
        Example: probability amplitude =  < state | ψ >
        """
        
        index = self.basis.index(base)
        return self.probabilityAmplitudes[index]
    
    def probability(self, base):
        
        """
        Return the probability of a given state.\n
        Example: probability =  < state | ψ >²
        """
        
        probabilityAmplitude = self.probabilityAmplitude(base)
        
        if isinstance(probabilityAmplitude, Complex):
            return probabilityAmplitude.conjugateSquare()
        elif isinstance(probabilityAmplitude, QuantumState):
            return probabilityAmplitude.totalProbability()
        else: TypeError()
    
    def conjugate(self):
        
        """
        Conjugate transpose the quantum state.\n
        Example: < ψ / = \ ψ >†
        """
        
        self.probabilityAmplitudes = [ probabilityAmplitude.conjugate() for probabilityAmplitude in self.probabilityAmplitudes ]
        
        return self
    
    def probabilityDensity(self):
        
        """
        Convert the quantum state to probability density distribution.\n
        Example: probability density = ψ* ψ
        """
    
        def probabilityDensityOfAmplitude(probabilityAmplitude):
            
            if isinstance(probabilityAmplitude, Complex):
                return probabilityAmplitude.conjugateSquare()
            elif isinstance(probabilityAmplitude, QuantumState):
                return probabilityAmplitude.probabilityDensity()
            else: TypeError()
        
        return [ probabilityDensityOfAmplitude(probabilityAmplitude) for probabilityAmplitude in self.probabilityAmplitudes ]
    
    def probabilityAmplitudeOfColapse(self, other):
        
        """
        Probability amplitude of this quantum state
        collapsing into another state.\n
        Example: < ϕ | ψ >
        """
        
        if isinstance(other, QuantumState):
            
            if self.basis == other.basis:
                
                probability = complex.zero
                
                for base in self.basis:
                    
                    probability += other.probabilityAmplitude(base).conjugate() * self.probabilityAmplitude(base)
                    
                return probability.real
            
            else: raise AttributeError()
        
        else: raise AttributeError()
    
    def probabilityOfColapse(self, other):
        
        """
        Probability of this quantum state
        collapsing into another state.\n
        Example: < ϕ | ψ >
        """
        
        if isinstance(other, QuantumState): return self.probabilityAmplitudeOfColapse(other).congugateSquare() 
        else: raise AttributeError()
    
    def ket(self):
        
        """
        Return quantum state as a ket. Type of
        the returned ket is ComplexMatrix.\n
        Example: \ ψ > = [ . . . ]
        """
        
        ket = []
        
        if all(isinstance(probabilityAmplitude, Complex) for probabilityAmplitude in self.probabilityAmplitudes):
            
            ket =  [self.probabilityAmplitudes]
        
        elif all(isinstance(probabilityAmplitude, QuantumState) for probabilityAmplitude in self.probabilityAmplitudes):
            
            ket = [ probabilityAmplitude.ket().matrix[0] for probabilityAmplitude in self.probabilityAmplitudes ]
        
        else: raise AttributeError()
        
        return CompexMatrix(ket)

    def bra(self):
        
        """
        Return quantum state as a bra. Type of
        the returned bra is ComplexMatrix.\n
        Example: < ψ / = [ ' ' ' ]
        """
        
        return self.conjugate().ket().transpose()

    def apply(self, operator: Operator):
        
        """
        Apply operator to the quantum state.\n
        Example: \ ψ > => operator \ ψ >
        """
        
        if operator.isMatrix and self.ket().rows < 2:
            
            probabilityAmplitudes = (operator.matrix @ self.ket()).matrix[0]
            
            return QuantumState(probabilityAmplitudes, self.basis)
        
        elif operator.type == 'momentum':
            
            # momentum shit here
            
            pass
        
        else: raise ValueError()
   
    def timeEvolve(self, hamiltonian: Operator):
        
        """
        Calculate how the quantum state changes
        over small interval of time with a given
        potential. This returns the next state.\n
        Example: \ ψ > => [ 1 - i/ℏ H Δt ] \ ψ >
        """
        
        deltaT = constants.delta
        N = len(self)
        
        timeEvolutionOperator = complexmatrix.identity((N, N)) - hamiltonian.scale(complex.i * deltaT / constants.hbar)
        
        result = self.apply(timeEvolutionOperator)
        return QuantumState(result.probabilityAmplitudes, result.basis)