import math
import complex

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
    
    def __init__(self, _probabilityAmplitudes, _basis):
        
        if len(_basis) == len(_probabilityAmplitudes):
            
            self.basis = _basis
            self.probabilityAmplitudes = _probabilityAmplitudes
        
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