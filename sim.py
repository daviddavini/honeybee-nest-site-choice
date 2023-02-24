import numpy as np

t_0 = 0
t_f = 1

NUM_STEPS = 1000
beta_1 = 0.6
beta_2 = 0.6
gamma = 0.3
# lambdaa = 0.3
delta = 0.5
alpha = 0

dt = (t_f - t_0) / NUM_STEPS

t = t_0
X = 100
Y_1 = 1
Y_2 = 0
Z_1 = 0
Z_2 = 0
N = X + Y_1 + Y_2 + Z_1 + Z_2

for i in range(NUM_STEPS):
    t += dt
    X += dt * (- beta_1 * X * Y_1 - beta_2 * X * Y_2)
    Y_1 += dt * (beta_1 * X * Y_1 - gamma * Y_1 + delta * beta_1 * Y_1 * Z_1 + alpha * beta_1 * Y_1 * Z_2)
    Y_2 += dt * (beta_2 * X * Y_2 - gamma * Y_2 + delta * beta_2 * Y_2 * Z_2 + alpha * beta_2 * Y_2 * Z_1)
    Z_1 += dt * (gamma * Y_1 - delta * beta_1 * Y_1 * Z_1 - alpha * beta_2 * Y_2 * Z_1)
    Z_2 += dt * (gamma * Y_2 - delta * beta_2 * Y_2 * Z_2 - alpha * beta_1 * Y_1 * Z_2)
    print(i, f"{Z_1:.1f}", f"{Y_1:.1f}", X, f"{Y_2:.1f}", f"{Z_2:.1f}", sep='\t')