import numpy as np
import matplotlib.pyplot as plt
#from sage.crypto.sbox import SBox

def henon_map(x, y, a=1.4, b=0.3):
    x_new = 1 - a * x**2 + y
    y_new = b * x
    return x_new, y_new

def lyapunov_exponent(x0, y0, a, b, n):
    sum = 0
    for i in range(n):
        x0, y0 = henon_map(x0, y0, a, b)
        sum += np.log(np.abs(a - 2 * a * x0))
    return sum / n

# Bifurcation Diagram Parameters
a_values = np.linspace(1.0, 1.4, 500)  # Range
b = 0.3  # Fixed value of b
iterations = 1000  
last = 100  # Number of iterations to plot
x0, y0 = 0.1, 0.1  

# Lyapunov Exponent Parameters
lyapunov_iterations = 1000  # 

# Prepare data for bifurcation diagram
x_bifurcation = np.zeros((len(a_values), last))

# Prepare data for Lyapunov exponent
lyapunov_exponents = np.zeros(len(a_values))

for i, a in enumerate(a_values):
    x_temp, y_temp = x0, y0
    
    # Calculate bifurcation diagram values
    for _ in range(iterations - last):
        x_temp, y_temp = henon_map(x_temp, y_temp, a, b)
    for j in range(last):
        x_temp, y_temp = henon_map(x_temp, y_temp, a, b)
        x_bifurcation[i, j] = x_temp
    
    # Calculate Lyapunov exponent
    lyapunov_exponents[i] = lyapunov_exponent(x0, y0, a, b, lyapunov_iterations)

# Plot Bifurcation Diagram (a vs x)
plt.figure(figsize=(10, 6))
for i in range(len(a_values)):
    plt.plot([a_values[i]] * last, x_bifurcation[i, :], ',k', alpha=0.25)
plt.xlabel('a')
plt.ylabel('x')
plt.title('Bifurcation Diagram for Hénon Map')
plt.grid(True)
plt.show()

# Plot Lyapunov Exponent Diagram (a vs λ)
plt.figure(figsize=(10, 6))
plt.plot(a_values, lyapunov_exponents, '-b', linewidth=0.5)
plt.xlabel('a')
plt.ylabel('Lyapunov Exponent')
plt.title('Lyapunov Exponent Diagram for Hénon Map')
plt.grid(True)
plt.show()
