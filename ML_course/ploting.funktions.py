import numpy as np
import matplotlib.pyplot as pl
#Funktion
def f (x): 
    y =3/( 1+ x) 
    return y
def g (x):
    y = x**3 + 5*x 
    return y
def h (x): 
    y = x*2
    return y 

x_data = np.linspace(-3, 3 ,100)
f_data = f( x_data )
g_data = g( x_data )
h_data = h( x_data )

pl.plot ( x_data , f_data, lw = 2 )
pl.plot ( x_data , g_data)
pl.plot ( x_data , h_data)
pl.xlabel('X')
pl.ylabel('Y')
pl.title('Funktions')
pl.show()

#lw - kolko e debela liniqta n a grafikata
"""np . linspace (0 ,0.5 ,6)
führt somit zu folgender Ausgabe.
array ([0. , 0.1 , 0.2 , 0.3 , 0.4 , 0.5])
Pyrvata stoinost kazva ot kude pochvame
Vtorata koga svyrshvame
Tretata kolko stojnosti da vzemem
"""