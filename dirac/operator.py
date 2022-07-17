from ast import operator
import dirac.complex as complex
from dirac.complex import Complex
import dirac.complexmatrix as complexmatrix
from dirac.complexmatrix import ComplexMatrix
import dirac.constants as constants

class Operator:
    
    def __init__(self, operator = []):
        
        if isinstance(operator, str):
            
            self.isMatrix = False
            self.isComposed = False
            self.matrix = None
            self.composition = []
            self.factor = None
            self.type = operator
        
        elif isinstance(operator, ComplexMatrix):
    
            self.isMatrix = True
            self.isComposed = False
            self.matrix = operator
            self.composition = []
            self.factor = None
            self.type = 'matrix'
        
        elif isinstance(operator, Complex):
            
            self.isMatrix = False
            self.isComposed = False
            self.matrix = None
            self.composition = []
            self.factor = operator
            self.type = 'factor'
        
        elif isinstance(operator, list):
            
            if all(isinstance(element, Operator) for element in operator):
                self.isMatrix = False
                self.isComposed = True
                self.matrix = None
                self.composition = operator
                self.factor = None
                self.type = 'composed'
            else: raise TypeError()
            
        else: raise AttributeError()
        
    def scale(self, factor: Complex):
        
        if self.isMatrix: return Operator(self.matrix.scale(factor))
        else: raise TypeError()
        
    def specialize(self, type):
        
        self.type = type
        return self

pauliXMatrix = ComplexMatrix([ [complex.zero, complex.one], [complex.one, complex.zero] ])
pauliYMatrix = ComplexMatrix([ [complex.zero, complex.i], [-complex.i, complex.zero] ])
pauliZMatrix = ComplexMatrix([ [complex.one, complex.zero], [complex.zero, -complex.one] ])

pauliX = Operator(pauliXMatrix)
pauliY = Operator(pauliYMatrix)
pauliZ = Operator(pauliZMatrix)

spinX = pauliX.scale(constants.halfhbar)
spinY = pauliY.scale(constants.halfhbar)
spinZ = pauliZ.scale(constants.halfhbar)

hadamardMatrix = ComplexMatrix([ [complex.one, complex.one], [complex.one, -complex.one] ]).scale(complex.roothalf)
hadamard = Operator(hadamardMatrix)


def position(positionBasis):
    
    operator = Operator(complexmatrix.diagonal(positionBasis))
    operator.specialize('position')
    return operator

momentum = Operator('momentum')
momentumSquared = Operator('momentum squared')

def kenetic(mass: float):
    
    operator = Operator([momentumSquared, Operator(complex.half / complex.ToComplex(mass))])
    operator.specialize('kenetic')
    return operator

def potential(potentialField: list):
    
    potentialField = complexmatrix.diagonal(potentialField)
    operator = Operator(potentialField)
    operator.specialize('potential')
    return operator

def comutator(leftOperator: Operator, rightOperator: Operator):
    
    if leftOperator.isMatrix and rightOperator.isMatrix:
        
        comutatorMatrix = (leftOperator.matrix @ rightOperator.matrix) - (rightOperator.matrix @ leftOperator.matrix)
        return Operator(comutatorMatrix)
    
    elif leftOperator.type == 'position' and rightOperator.type == 'momentum': return complex.i * constants.hbar
    
    elif leftOperator.type == 'momentum' and rightOperator.type == 'position': return -complex.i * constants.hbar
    
    else: raise AttributeError()
    
def anticomutator(leftOperator: Operator, rightOperator: Operator):
    
    if leftOperator.isMatrix and rightOperator.isMatrix:
        
        comutatorMatrix = (leftOperator.matrix @ rightOperator.matrix) + (rightOperator.matrix @ leftOperator.matrix)
        return Operator(comutatorMatrix)
    
    else: raise AttributeError()