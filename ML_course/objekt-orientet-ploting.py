import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y = x**2
z = 5*x - 6

# ako ne slojim broi redove i koloni dvete grafiki ste se plotnat na edno
fig,axis = plt.subplots(nrows = 1, ncols = 2)
axis[0].plot(x,y)
axis[1].plot(x,z)

axis[0].set_xlabel('X')
axis[0].set_ylabel('Y')
axis[0].set_title('Top sym')

axis[1].set_xlabel('X')
axis[1].set_ylabel('Y')
axis[1].set_title('Top sym Vol.2')

plt.tight_layout()

