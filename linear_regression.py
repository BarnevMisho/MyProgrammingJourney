import numpy as np
import matplotlib.pyplot as plt

x  = [10, 12, 13, 14, 18, 20, 25, 26]
y  = [813, 781, 722, 603, 582, 551, 510, 330]

dg = 1
[a,b] = np.polyfit(x, y, dg)
print(f"{a :.3f}", end = " ")
print(f"{b :.3f}", end = " ")

def f(r):
    p = a * r + b 
    return p

x_data = np.linspace (9, 27, 100)
f_data = f(x_data);

plt.figure()
plt.plot(x_data , f_data , lw = 2) 
plt.plot(x, y, "o") 
plt.xlabel('X')
plt.ylabel('Y')
plt.title('linear regression')
plt.show()


"""
# alternativen podhod s vgradeni funkcii
deg = int(input("regression degree: "))
p = np.polyfit(x, y, deg)
g_data = np.polyval(p, x)
plt.plot(x , g_data , lw = 2) 
plt.plot( x, y, "o") 
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
"""

# sedma zadacha
"""
def revenue(m):
    s = (a * m + b ) * m
    return s

data = np.linspace (9, 30, 100)
y_data = revenue(data)
plt.figure()
plt.plot(data, y_data, lw = 2) 
for n in range(len(x)):
    plt.plot(x[n], y[n]*x[n], "o") 
plt.show   
"""
