import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

NUM_STEPS = 1000

def approx_system(init_conds, params):
    [X, Y_1, Y_2] = init_conds
    Z_1 = 0
    Z_2 = 0
    [beta_1, beta_2, gamma, delta, alpha_1, alpha_2] = params
    t_0 = 0
    t_f = 10
    dt = (t_f - t_0) / NUM_STEPS

    t = t_0
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

    values = [tall, Xall, Y_1all, Y_2all, Z_1all, Z_2all]
    return values

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.6)
default_value = 0.1
default_X = 10
default_Y_1 = 0.5
default_Y_2 = 0.1
default_init_conds = [default_X, default_Y_1, default_Y_2]
default_alpha_1 = 3.14 # default_value
default_alpha_2 = 2.71 # default_value
default_beta_1 = 1.41 # default_value
default_beta_2 = 2.71 # default_value
default_gamma = 1.0 # default_value
default_delta = 0.29 # default_value
default_params = [default_beta_1, default_beta_2, default_gamma, default_delta, default_alpha_1, default_alpha_2]
[t, X, Y_1, Y_2, Z_1, Z_2] = approx_system(default_init_conds, default_params)
l_X, = plt.plot(t, X, lw=2, label="$X$")
l_Y_1, = plt.plot(t, Y_1, lw=2, label="$Y_1$")
l_Y_2, = plt.plot(t, Y_2, lw=2, label="$Y_2$")
l_Z_1, = plt.plot(t, Z_1, lw=2, label="$Z_1$")
l_Z_2, = plt.plot(t, Z_2, lw=2, label="$Z_2$")
plt.legend()
# plt.axis([t[0], t[-1], -10, 10])

axcolor = 'lightgoldenrodyellow'
axbeta_1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axbeta_2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_gamma = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_delta = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_alpha_1 = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=axcolor)
ax_alpha_2 = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)
axX = plt.axes([0.25, 0.4, 0.65, 0.03], facecolor=axcolor)
axY_1 = plt.axes([0.25, 0.45, 0.65, 0.03], facecolor=axcolor)
axY_2 = plt.axes([0.25, 0.5, 0.65, 0.03], facecolor=axcolor)

valmin = 0.0
param_max = 5.0
init_cond_max = 10.0
sX = Slider(axX, '$X$', valmin, init_cond_max, valinit=default_X)
sY_1 = Slider(axY_1, '$Y_1$', valmin, init_cond_max, valinit=default_Y_1)
sY_2 = Slider(axY_2, '$Y_2$', valmin, init_cond_max, valinit=default_Y_2)
sbeta_1 = Slider(axbeta_1, '$\\beta_1$', valmin, param_max, valinit=default_beta_1)
sbeta_2 = Slider(axbeta_2, '$\\beta_2$', valmin, param_max, valinit=default_beta_2)
sgamma = Slider(ax_gamma, '$\\gamma$', valmin, param_max, valinit=default_gamma)
sdelta = Slider(ax_delta, '$\\delta$', valmin, param_max, valinit=default_delta)
salpha_1 = Slider(ax_alpha_1, '$\\alpha_1$', valmin, param_max, valinit=default_alpha_1)
salpha_2 = Slider(ax_alpha_2, '$\\alpha_2$', valmin, param_max, valinit=default_alpha_2)
sliders = [sX, sY_1, sY_2, sbeta_1, sbeta_2, sgamma, sdelta, salpha_1, salpha_2]

def update(val):
    X = sX.val
    Y_1 = sY_1.val
    Y_2 = sY_2.val
    init_conds = [X, Y_1, Y_2]
    beta_1 = sbeta_1.val
    beta_2 = sbeta_2.val
    gamma = sgamma.val
    delta = sdelta.val
    alpha_1 = salpha_1.val
    alpha_2 = salpha_2.val
    params = [beta_1, beta_2, gamma, delta, alpha_1, alpha_2]
    [t, X, Y_1, Y_2, Z_1, Z_2] = approx_system(init_conds, params)
    l_X.set_ydata(X)
    l_Y_1.set_ydata(Y_1)
    l_Y_2.set_ydata(Y_2)
    l_Z_1.set_ydata(Z_1)
    l_Z_2.set_ydata(Z_2)
    fig.canvas.draw_idle()

for slider in sliders:
    slider.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()