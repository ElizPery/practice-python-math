from scipy.optimize import linprog

c = [-2, -9, -6]  # Target function - to maximum
A_ub = [
    [12, 6, 2],
    [12, 24, 18],
    [12, 18, 12],
    [0, 0, -1],
    [-1, 0, 0],
    [0, -1, 0],
]  # Coefficients for inequalities
b_ub = [320,192,180,0,0,0]  # Results for inequalities

print(linprog(c, A_ub, b_ub))  # Optimization