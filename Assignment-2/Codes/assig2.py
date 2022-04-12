import sympy as sp

x=sp.Symbol('x')

def M(x):

     return  3*x*x -10*x +3

def I(y):
      
    exp=sp.integrate(M(x),x) 
    #This does symbolic integration and hence cannot be used for computations in present state.
    #Lambdify converts symbolic expression to normal form, so that it cam be used for computations.
    k = sp.lambdify(x,exp)
    return k(y)

def C(x,c):

    return I(x)+c 

# We can use the fact C(1) =7 to calculate c and shall always call C along with c parameter

c = 7 - I(1)

#From now call of C(x,c) gives value of C(x) 

def A(x,c):
    return C(x,c)/x


print('M(x) is given to be ',M(x))

print('So, C(x) is ',sp.simplify(C(x,c)))

exp =sp.simplify(A(x,c))

print('And A(x) is',exp)