import numpy as np
from sage.crypto.sbox import SBox

# Henon map parameters
henon_a, henon_b = 1.4, 0.3

# Initialize chaotic numbers
x, y = 0.1, 0.1

# Number of iterations
max_iterations = 100

# Define the matrix size
n = 16
num_wolves = 5

# Initialize the population with 5 matrices with values in range (0, 255)
population = [np.random.randint(0, 256, size=(n, n)) for _ in range(num_wolves)]

# Lists to store A and C values
A_values = []
C_values = []

def henon_map(x, y, a=1.4, b=0.3):
    x_new = 1 - a * x**2 + y
    y_new = b * x
    return x_new, y_new

def calculate_nonlinearity(matrix_flat):
    S = SBox(matrix_flat)  # Initialize SBox with the flattened list
    return S.nonlinearity()

# Main loop for Henon map and nonlinearity calculation
for iteration in range(max_iterations):
    # Generate chaotic sequence
    x, y = henon_map(x, y, henon_a, henon_b)
    
    # Normalize chaotic sequence to [0, 1]
    x_norm = (x - min(x, y)) / (max(x, y) - min(x, y))
    
    # Decreasing a linearly from 2 to 0
    a = 2 - 2 * (iteration / max_iterations)
    
    # Calculate coefficients using normalized chaotic sequence
    A = 2 * a * x_norm - a
    C = abs(2 * y % 2.0)
    
    # Round A and C to 2 decimal places
    A = round(A, 2)
    C = round(C, 2)
    
    # Store A and C values
    A_values.append(A)
    C_values.append(C)
    
    # Print A and C values
    print(f"Iteration {iteration + 1}: A = {A}, C = {C}")

# Optional: Print all A and C values after the loop
print("\nAll A values:", A_values)
print("All C values:", C_values)

# Calculate the nonlinearity of each matrix in the population
nonlinearities = [(matrix, calculate_nonlinearity(matrix.flatten().tolist())) for matrix in population]

# Sort matrices by nonlinearity in descending order
nonlinearities.sort(key=lambda x: x[1], reverse=True)

# Identify alpha, beta, and delta
alpha = nonlinearities[0][0]
beta = nonlinearities[1][0]
delta = nonlinearities[2][0]
delta_nonlinearity = nonlinearities[2][1]

# Print matrices and their nonlinearities
print("\nMatrices and their nonlinearities:")
for i, (matrix, nonlinearity) in enumerate(nonlinearities):
    print(f"Matrix {i + 1}:\n{matrix}\nNonlinearity: {nonlinearity}\n")

# Print alpha, beta, and delta matrices
print("Alpha Matrix:\n", alpha)
print("Beta Matrix:\n", beta)
print("Delta Matrix:\n", delta)

# Iterate 100 times to perform the specified calculations
for iteration in range(100):
    Dalpha = np.abs(C_values[iteration] * alpha - alpha)
    Dbeta = np.abs(C_values[iteration] * alpha - beta)
    Ddelta = np.abs(C_values[iteration] * alpha - delta)
    
    Xalpha = alpha - A_values[iteration] * Dalpha
    Xbeta = alpha - A_values[iteration] * Dbeta
    Xdelta = alpha - A_values[iteration] * Ddelta
    
    X_t_plus_1_matrix = abs(np.round((Xalpha + Xbeta + Xdelta) / 3).astype(int))

    # Calculate the nonlinearity of X(t+1)
    X_t_plus_1_nonlinearity = calculate_nonlinearity(X_t_plus_1_matrix.flatten().tolist())
    
    # Print X(t+1) and its nonlinearity
    if(X_t_plus_1_nonlinearity > 80):
        print(f"\n Iteration {iteration + 1}:\n  X(t+1) =\n{X_t_plus_1_matrix}\nNonlinearity: {X_t_plus_1_nonlinearity}\n")
    
    # Check if the nonlinearity of X(t+1) is greater than that of delta
    if X_t_plus_1_nonlinearity > delta_nonlinearity:
        delta = X_t_plus_1_matrix
        delta_nonlinearity = X_t_plus_1_nonlinearity
        #print(f"Iteration {iteration + 1}: X(t+1) replaces Delta\n")
