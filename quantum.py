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
        
        probability = 0
        
        for probabilityAmplitude in self.probabilityAmplitudes:
            probability += probabilityAmplitude.conjugateSquare()
            
        return probability
    
    def normalize(self):
        
        normalizationFactor = self.totalProbability()
        
        self.probabilityAmplitudes = list(map(lambda amplitude: complex.ToComplex(math.sqrt(1 / normalizationFactor)) * amplitude, self.probabilityAmplitudes))
            
        return self
    
    def __init__(self, probabilityAmplitudes, basis):
        
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
    
    def probabilityAmplitude(self, base):
        
        index = self.basis.index(base)
        return self.probabilityAmplitudes[index]
    
    def probability(self, base): return self.probabilityAmplitude(base).conjugateSquare()
    
    def conjugate(self):
        
        self.probabilityAmplitudes = [ probabilitiAmplitude.conjugate() for probabilitiAmplitude in self.probabilityAmplitudes ]
        return self
    
    def __len__(self): return len(self.basis)
    
    def probabilityOfColapse(self, other):
        
        if self.basis == other.basis:
            
            probability = complex.zero
            
            for base in self.basis:
                
                probability += other.probabilityAmplitude(base).conjugate() * self.probabilityAmplitude(base)
                
            return probability.real
        
        else: raise AttributeError() 
    
    def ket(self): return CompexMatrix([self.probabilityAmplitudes])

    def bra(self): return[ [probabilityAmplitude.conjugate()] for probabilityAmplitude in self.probabilityAmplitudes ]

    def apply(self, operator):
        
       probabilityAmplitudes = (operator @ self.ket()).matrix[0]
       
       return WaveFunction(probabilityAmplitudes, self.basis)