import IPython . display as dp ;
import sympy as sp ;

sp . init_printing ();
x = sp.symbols ("x");
# Parameter :
p = 2*(3+3*sp.tan(x)**2)*sp.cos(x)**2
# Berechnungen :
f = sp.expand(p)
g = sp.factor(p)
h = sp.simplify(p)

dp.display(f)
print(f)
dp.display(g)
dp.display(h)

z = sp . symbols ("z");
gleichung = z**2 - z*15 + 50
antwort = sp.solve(gleichung, z)
dp.display(antwort)
print(antwort)