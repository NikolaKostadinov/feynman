import dirac.complex as complex
from dirac.complex import Complex
import dirac.complexmatrix as complexmatrix
from dirac.complexmatrix import CompexMatrix
import dirac.constants as constants

class Operator:
    
    def __init__(self, operator = []):
        
        if isinstance(operator, str):
            
            self.isMatrix = False
            self.matrix = None
            self.type = operator
        
        elif isinstance(operator, CompexMatrix):
    
            self.isMatrix = True
            self.matrix = operator
            self.type = 'matrix operator'
        
        else: raise AttributeError()
        
    def scale(self, factor: Complex):
        
        if self.isMatrix: return Operator(self.matrix.scale(factor))
        else: raise TypeError()
        
    def specialize(self, type):
        
        self.type = type
        return self

pauliXMatrix = CompexMatrix([ [complex.zero, complex.one], [complex.one, complex.zero] ])
pauliYMatrix = CompexMatrix([ [complex.zero, complex.i], [-complex.i, complex.zero] ])
pauliZMatrix = CompexMatrix([ [complex.one, complex.zero], [complex.zero, -complex.one] ])

pauliX = Operator(pauliXMatrix)
pauliY = Operator(pauliYMatrix)
pauliZ = Operator(pauliZMatrix)

spinX = pauliX.scale(constants.halfhbar)
spinY = pauliY.scale(constants.halfhbar)
spinZ = pauliZ.scale(constants.halfhbar)

hadamardMatrix = CompexMatrix([ [complex.one, complex.one], [complex.one, -complex.one] ]).scale(complex.roothalf)
hadamard = Operator(hadamardMatrix)

momentum = Operator('momentum')

def position(positionBasis):
    
    operator = Operator(complexmatrix.diagonal(positionBasis))
    operator.specialize('position')
    return operator

def comutator(leftOperator: Operator, rightOperator: Operator):
    
    if leftOperator.isMatrix and rightOperator.isMatrix:
        
        comutatorMatrix = (leftOperator.matrix @ rightOperator.matrix) - (rightOperator.matrix @ leftOperator.matrix)
        return Operator(comutatorMatrix)
    
    elif leftOperator.type == 'position' and rightOperator == momentum: return complex.i * constants.hbar
    
    elif leftOperator == momentum and rightOperator.type == 'position': return -complex.i * constants.hbar
    
    else: raise AttributeError()
    
def anticomutator(leftOperator: Operator, rightOperator: Operator):
    
    if leftOperator.isMatrix and rightOperator.isMatrix:
        
        comutatorMatrix = (leftOperator.matrix @ rightOperator.matrix) + (rightOperator.matrix @ leftOperator.matrix)
        return Operator(comutatorMatrix)
    
    else: raise AttributeError()