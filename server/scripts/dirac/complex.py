import math
from decimal import Decimal

def toPolar(x, y):
    
    X = Decimal(x)
    Y = Decimal(y) 
    r = math.sqrt( X**2 + Y**2 )
    theta = math.atan2(y, x)
    
    return r, theta

def toCartesian(r, theta):
    
    x = math.cos(theta) * r
    y = math.sin(theta) * r
    
    return x, y

class Complex:
    
    def __str__(self):
        
        if self.real < 0: realSign = '-'
        else: realSign = ''
        real = abs(self.real)
        
        if self.imaginary < 0: imaginarySign = '-'
        else: imaginarySign = '+'
        imaginary = abs(self.imaginary)
        
        return f'{realSign}{real} {imaginarySign} {imaginary}i'
    
    def __repr__(self): return self.__str__()
    
    def __init__(self, **kwargs):
        
        real = kwargs.get('real')
        imaginary = kwargs.get('imaginary')
        modulus = kwargs.get('modulus')
        argument = kwargs.get('argument')

        if real is not None and imaginary is not None: modulus, argument = toPolar(real, imaginary)
        elif modulus is not None and argument is not None: real, imaginary = toCartesian(modulus, argument)
        else: raise AttributeError('Incorrect attributes. Set real and imaginary or modulus and argument')
        
        self.real = real
        self.imaginary = imaginary
        self.modulus = modulus
        self.argument = argument
    
    def __add__(complexLeft, complexRight):
        
        realSum = complexLeft.real + complexRight.real
        imaginarySum = complexLeft.imaginary + complexRight.imaginary
        
        return Complex(real=realSum, imaginary=imaginarySum)
    
    def __sub__(complexLeft, complexRight):
        
        realDif = complexLeft.real - complexRight.real
        imaginaryDif = complexLeft.imaginary - complexRight.imaginary
        
        return Complex(real=realDif, imaginary=imaginaryDif)
    
    def __iadd__(self, other): return self + other    

    def __mul__(complexLeft, complexRight):
        
        modulusProd = complexLeft.modulus * complexRight.modulus
        argumentProd = complexLeft.argument + complexRight.argument
        
        return Complex(modulus=modulusProd, argument=argumentProd)
    
    def _imult__(self, other): return self * other
    
    def __truediv__(complexLeft, complexRight):
        
        modulusDiv = complexLeft.modulus / complexRight.modulus
        argumentDiv = complexLeft.argument - complexRight.argument
        
        return Complex(modulus=modulusDiv, argument=argumentDiv)

    def __itruediv__(self, other): return self / other

    def __pos__(self): return self
    
    def __neg__(self): return Complex(real=-self.real, imaginary=-self.imaginary)

    def conjugate(self):
        
        real = self.real
        imaginary = - self.imaginary
        
        return Complex(real=real, imaginary=imaginary)
        
    def conjugateSquare(self):
        
        conjugateSq = self.conjugate() * self
        return abs(conjugateSq.real)
    
    def square(self): return self * self

def ToComplex(number): return Complex(real=number, imaginary=0)

def ToImaginary(number): return Complex(real=0, imaginary=number)

def exp(comlexNumber: Complex):
    
    return Complex(modulus = math.exp(comlexNumber.real), argument = comlexNumber.imaginary)

zero = ToComplex(0)
one = ToComplex(1)
i = ToImaginary(1)
e = ToComplex(math.e)
pi = ToComplex(math.pi)
tau = ToComplex(2 * math.pi)
halfpi = ToComplex(.5 * math.pi)
two = ToComplex(2)
half = ToComplex(.5)
roothalf = ToComplex(math.sqrt(.5))
rootthird = ToComplex(math.sqrt(1/3))