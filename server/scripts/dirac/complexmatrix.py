import dirac.complex as complex

class ComplexMatrix:
    
    def __init__(self, matrix):
        
        self.rows = len(matrix[0])
        self.columns = len(matrix)
        
        self.size = self.rows, self.columns
        
        self.matrix = matrix
        
    def __str__(self):
        
        matrixString = ''
        
        for i in range(self.rows):
            
            for j in range(self.columns):
                
                matrixString += str(self.matrix[j][i])
                matrixString += ' '
            
            matrixString += '\n'
            
        return matrixString
    
    def __repr__(self): return str(self)
    
    def __add__(matrixLeft, matrixRight):
        
        if matrixLeft.size == matrixRight.size:
            
            sum = [ [ 0 for _ in range(matrixLeft.rows) ] for _ in range(matrixLeft.columns) ]
            
            for i in range(matrixLeft.columns):
                
                for j in range(matrixLeft.rows):
                
                    sum[i][j] = matrixLeft.matrix[i][j] + matrixRight.matrix[i][j]
            
            return ComplexMatrix(sum)
            
        else: raise IndexError()
        
    def __sub__(matrixLeft, matrixRight):
        
        if matrixLeft.size == matrixRight.size:
            
            sum = [ [ 0 for _ in range(matrixLeft.rows) ] for _ in range(matrixLeft.columns) ]
            
            for i in range(matrixLeft.columns):
                
                for j in range(matrixLeft.rows):
                
                    sum[i][j] = matrixLeft.matrix[i][j] - matrixRight.matrix[i][j]
            
            return ComplexMatrix(sum)
            
        else: raise IndexError()
        
    def __matmul__(matrixLeft, matrixRight):
        
        if matrixLeft.columns == matrixRight.rows:
            
            mul = [ [ complex.zero for _ in range(matrixLeft.rows) ] for _ in range(matrixRight.columns) ]
            
            for i in range(matrixRight.columns):
                
                for j in range(matrixLeft.rows):
                
                    sum = complex.zero
                    for n in range(matrixLeft.columns):
                        sum += matrixRight.matrix[i][n] * matrixLeft.matrix[n][j]
                    mul[i][j] = sum
            
            return ComplexMatrix(mul)
        
        else: raise IndexError()
        
    def transpose(self):
        
        transposed = self.matrix
        
        for i in range(1, self.columns):
                
            for j in range(self.rows):
                
                transposed[i][j], transposed[j][i] = transposed[j][i], transposed[i][j]
        
        return ComplexMatrix(transposed)
    
    def apply(self, function):
        
        for i in range(self.columns):
                
            for j in range(self.rows):
                
                self.matrix[i][j] = function(self.matrix[i][j])
                
        return self
    
    def scale(self, factor): return self.apply(lambda x: factor * x)    

def identity(size):
    
    matrix = []
    
    for i in range(size[0]):
        
        column = []
        for j in range(size[1]):
            
            if i == j: column.append(complex.one)
            else: column.append(complex.zero)
            
        matrix.append(column)
        
    return ComplexMatrix(matrix)

def diagonal(diagonal):
    
    matrix = []
    size = len(diagonal)
    
    for i in range(size):
        
        column = []
        for j in range(size):
            
            if i == j: column.append(diagonal[i])
            else: column.append(complex.zero)
            
        matrix.append(column)
        
    return ComplexMatrix(matrix)

def wideDiagonal(diagonalValue, offsetValue, size):
    
    matrix = []
    
    for i in range(size[0]):
        
        column = []
        for j in range(size[1]):
            
            if i == j: column.append(diagonalValue)
            elif i+1 == j or i == j+1 or i-1 == j or i == j-1: column.append(offsetValue)
            else: column.append(complex.zero)
        matrix.append(column)
        
    return ComplexMatrix(matrix)