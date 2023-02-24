import numpy as np
from matplotlib import pyplot as plt

t_0 = 0
t_f = 20

NUM_STEPS = 1000
beta_1 = 0.3
beta_2 = 0.9
gamma = 0.4
delta = 0.5
alpha_1 = 0.5
alpha_2 = 0.3

dt = (t_f - t_0) / NUM_STEPS

t = t_0
X = 10
Y_1 = 5
Y_2 = 1
Z_1 = 0
Z_2 = 0
N = X + Y_1 + Y_2 + Z_1 + Z_2

tall = [t]
Xall = [X]
Y_1all = [Y_1]
Y_2all = [Y_2]
Z_1all = [Z_1]
Z_2all = [Z_2]

for i in range(NUM_STEPS):
    t += dt
    # direct model
    X += dt * (- beta_1 * X * Y_1 - beta_2 * X * Y_2)
    Y_1 += dt * (beta_1 * X * Y_1 - gamma * Y_1 + delta * beta_1 * Y_1 * Z_1 + alpha_2 * beta_1 * Y_1 * Z_2)
    Y_2 += dt * (beta_2 * X * Y_2 - gamma * Y_2 + delta * beta_2 * Y_2 * Z_2 + alpha_1 * beta_2 * Y_2 * Z_1)
    Z_1 += dt * (gamma * Y_1 - delta * beta_1 * Y_1 * Z_1 - alpha_1 * beta_2 * Y_2 * Z_1)
    Z_2 += dt * (gamma * Y_2 - delta * beta_2 * Y_2 * Z_2 - alpha_2 * beta_1 * Y_1 * Z_2)
    tall.append(t)
    Xall.append(X)
    Y_1all.append(Y_1)
    Y_2all.append(Y_2)
    Z_1all.append(Z_1)
    Z_2all.append(Z_2)
    print(i, f"{Z_1:.1f}", f"{Y_1:.1f}", X, f"{Y_2:.1f}", f"{Z_2:.1f}", sep='\t')

tall = np.array(tall)
Xall = np.array(Xall)
Y_1all = np.array(Y_1all)
Y_2all = np.array(Y_2all)
Z_1all = np.array(Z_1all)
Z_2all = np.array(Z_2all)

plt.plot(tall, Xall, label="$X$")
plt.plot(tall, Y_1all, label="$Y_1$")
plt.plot(tall, Y_2all, label="$Y_2$")
plt.plot(tall, Z_1all, label="$Z_1$")
plt.plot(tall, Z_2all, label="$Z_2$")
plt.legend()
plt.savefig("test")