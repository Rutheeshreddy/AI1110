import sympy as sym

x = sym.Symbol('x')

def g(x) :

        return x*x*x 

g_2 = sym.diff(sym.diff(g(x),x),x)

g_2 = sym.lambdify(x,g_2)
E = g(10) + (g_2(10)*4)/2
print('Required value is',E)
