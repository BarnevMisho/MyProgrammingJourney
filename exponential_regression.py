import numpy as np
import matplotlib.pyplot as plt

x  = [273, 412, 556, 990, 1638, 1709, 3550]
y  = [976.9, 973.6, 955.5, 902.3, 834.2, 824.7, 649]

[a,b] = np.polyfit(x, np.log(y), 1)
print(f"{a :.6f}", end = " ")
print(f"{b :.3f}")

def f(r):
    p = np.exp(b) * np.exp(a*r)
    return p

x_data = np.linspace (270, 3600, 1000)
f_data = f(x_data);

plt.figure()
plt.plot(x_data , f_data , lw = 2) 
plt.plot(x, y, "o")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('exponential regression')
plt.show()

