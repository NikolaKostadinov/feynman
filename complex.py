import math

def toPolar(x, y):
    
    r = math.sqrt( x**2 + y**2 )
    
    if x != 0:
        slope = y / x
        theta = math.atan(slope)
    else:
        theta = .5 * math.pi
    
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

    def conjugate(self):
        
        real = self.real
        imaginary = - self.imaginary
        
        return Complex(real=real, imaginary=imaginary)
        
    def conjugateSquare(self):
        
        conjugateSq = self.conjugate() * self
        return abs(conjugateSq.real)

zero = Complex(real=0, imaginary=0)
one = Complex(real=1, imaginary=0)
i = Complex(real=0, imaginary=1)
e = Complex(real=math.e, imaginary=0)

def ToComplex(number): return Complex(real=number, imaginary=0)