import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

STEPS_PER_TIME = 100
# STEPS_PER_TIME = 10

def approx_system_i(init_conds, params, t_i):
    [Y1_0] = init_conds
    X_0 = 1 - Y1_0
    Z1_0 = 0
    [b1, g, d, l, p] = params

    t_0 = 0
    num_steps = int((t_i - t_0) * STEPS_PER_TIME)+1
    dt = (t_i - t_0) / num_steps

    t_arr = np.linspace(t_0, t_i, num_steps+1)
    X_arr = np.ones(num_steps+1)*X_0
    Y1_arr = np.ones(num_steps+1)*Y1_0
    Z1_arr = np.ones(num_steps+1)*Z1_0

    for i in range(num_steps):
        X = X_arr[i]
        Y1 = Y1_arr[i]
        Z1 = Z1_arr[i]
        X_arr[i+1] = X + dt * (-b1*X*Y1 + p*l*Z1)
        Y1_arr[i+1] = Y1 + dt * (b1*X*Y1 - g*Y1 + d*b1*Y1*Z1)
        Z1_arr[i+1] = Z1 + dt * (g*Y1 - d*b1*Y1*Z1 - p*l*Z1)

    values = np.array([t_arr, X_arr, Y1_arr, Z1_arr])

    return values


def approx_system_f(init_conds, params, t_i, t_f):
    [X_0, Y1_0, Y2_0, Z1_0] = init_conds
    Z2_0 = 0
    [b1, b2, g, d, a, l, p] = params

    t_0 = 0
    num_steps = int((t_f - t_i) * STEPS_PER_TIME)+1
    dt = (t_f - t_i) / num_steps

    t_arr = np.linspace(t_i, t_f, num_steps+1)
    X_arr = np.ones(num_steps+1)*X_0
    Y1_arr = np.ones(num_steps+1)*Y1_0
    Y2_arr = np.ones(num_steps+1)*Y2_0
    Z1_arr = np.ones(num_steps+1)*Z1_0
    Z2_arr = np.ones(num_steps+1)*Z2_0

    for i in range(num_steps):
        X = X_arr[i]
        Y1 = Y1_arr[i]
        Y2 = Y2_arr[i]
        Z1 = Z1_arr[i]
        Z2 = Z2_arr[i]
        X_arr[i+1] = X + dt * (-b1*X*Y1 - b2*X*Y2 + p*l*Z1 + p*l*Z2)
        Y1_arr[i+1] = Y1 + dt * (b1*X*Y1 - g*Y1 + d*b1*Y1*Z1 + (1-p)*a*b1*Y1*Z2)
        Y2_arr[i+1] = Y2 + dt * (b2*X*Y2 - g*Y2 + d*b2*Y2*Z2 + (1-p)*a*b2*Y2*Z1)
        Z1_arr[i+1] = Z1 + dt * (g*Y1 - d*b1*Y1*Z1 - p*l*Z1 - (1-p)*a*b2*Y2*Z1)
        Z2_arr[i+1] = Z2 + dt * (g*Y2 - d*b2*Y2*Z2 - p*l*Z2 - (1-p)*a*b1*Y1*Z2)

    values = np.array([t_arr, X_arr, Y1_arr, Y2_arr, Z1_arr, Z2_arr])

    return values

# figsize = (12, 10)
figsize = (8, 6)
fig, ax = plt.subplots(1, 2, figsize=figsize, sharey=True)
plt.subplots_adjust(left=0.1, bottom=.5)
def_t_i = 500
def_t_f = 1000
def_Y1 = 10
def_Y2 = 0
def_b1 = 1.0
def_b2 = 1.0
def_g = 1.0
def_d = 1.0
def_a = 1.0
def_l = 1.0
def_p = 1.0

def_init_conds_i = [def_Y1]
def_params_i = [def_b1, def_g, def_d, def_l, def_p]
[t_arr, X_arr, Y1_arr, Z1_arr] = approx_system_i(def_init_conds_i, def_params_i, def_t_i)
l0_X, = ax[0].plot(t_arr, X_arr, lw=2, label="$X$", color="blue")
l0_Y1, = ax[0].plot(t_arr, Y1_arr, lw=2, label="$Y1$", color="orange")
l0_Z1, = ax[0].plot(t_arr, Z1_arr, lw=2, label="$Z1$", color="green")
ax[0].set_xlim(0, def_t_i)
max_elt = 1.1 * max([np.max(X_arr), np.max(Y1_arr), np.max(Z1_arr)])
ax[0].set_ylim(0, max_elt)
ax[0].legend()

def_init_conds_f = [X_arr[-1], Y1_arr[-1], def_Y2, Z1_arr[-1]]
def_params_f = [def_b1, def_b2, def_g, def_d, def_a, def_l, def_p]
[t_arr, X_arr, Y1_arr, Y2_arr, Z1_arr, Z2_arr] = approx_system_f(def_init_conds_f, def_params_f, def_t_i, def_t_f)
l1_X, = ax[1].plot(t_arr, X_arr, lw=2, label="$X$", color="blue")
l1_Y1, = ax[1].plot(t_arr, Y1_arr, lw=2, label="$Y1$", color="orange")
l1_Y2, = ax[1].plot(t_arr, Y2_arr, lw=2, label="$Y2$", color="red")
l1_Z1, = ax[1].plot(t_arr, Z1_arr, lw=2, label="$Z1$", color="green")
l1_Z2, = ax[1].plot(t_arr, Z2_arr, lw=2, label="$Z2$", color="purple")
ax[1].set_xlim(def_t_i, def_t_f)
max_elt = 1.1 * max([np.max(X_arr), np.max(Y1_arr), np.max(Y2_arr), np.max(Z1_arr), np.max(Z2_arr)])
ax[1].set_ylim(0, max_elt)
ax[1].legend()

plots = [l0_X, l0_Y1, l0_Z1, l1_X, l1_Y1, l1_Y2, l1_Z1, l1_Z2]
# plt.legend()
# plt.axis([t[0], t[-1], 0, 1])

axcolor = 'lightgoldenrodyellow'
[ax_p, ax_a, ax_l, ax_d, ax_g, ax_b2, ax_b1, ax_Y2, ax_Y1, ax_t_f, ax_t_i] = [
    plt.axes([0.3, 0.1 + i*0.03, 0.6, 0.03], facecolor=axcolor) for i in range(11) 
]

valmin = 0.0
time_max = 1000
param_max = 5.0
init_cond_max = 100
random_max = 1.0
s_t_i = Slider(ax_t_i, '$t_f$ (Intermediate Time)', 0.1, time_max, valinit=def_t_i)
s_t_f = Slider(ax_t_f, '$t_f$ (Final Time)', 0.1, time_max, valinit=def_t_f)
s_Y1 = Slider(ax_Y1, '$Y_1$ (Nest 1 Initial Supporters)', valmin, init_cond_max, valinit=def_Y1)
s_Y2 = Slider(ax_Y2, '$Y_2$ (Nest 2 Initial Supporters)', valmin, init_cond_max, valinit=def_Y2)
s_b1 = Slider(ax_b1, '$\\beta_1$ (Nest 1 Persuasion Rate)', valmin, param_max, valinit=def_b1)
s_b2 = Slider(ax_b2, '$\\beta_2$ (Nest 2 Persuasion Rate)', valmin, param_max, valinit=def_b2)
s_g = Slider(ax_g, '$\\gamma$ (Dance Cease Rate)', valmin, param_max, valinit=def_g)
s_d = Slider(ax_d, '$\\delta$ (Re-dance Rate)', valmin, param_max, valinit=def_d)
s_a = Slider(ax_a, '$\\alpha$ (Direct-switching Rate)', valmin, param_max, valinit=def_a)
s_l = Slider(ax_l, '$\\lambda$ (Indirect-switching Rate)', valmin, param_max, valinit=def_l)
s_p = Slider(ax_p, '$\\rho$ (Probability of Indirect-switching)', valmin, random_max, valinit=def_p)
sliders = [s_t_i, s_t_f, s_Y1, s_Y2, s_b1, s_b2, s_g, s_d, s_a, s_l, s_p]

def update(val):
    t_i = s_t_i.val
    t_f = s_t_f.val
    Y1 = s_Y1.val
    Y2 = s_Y2.val
    b1 = s_b1.val
    b2 = s_b2.val
    g = s_g.val
    d = s_d.val
    a = s_a.val
    l = s_l.val
    p = s_p.val

    init_conds_i = [Y1]
    params_i = [b1, g, d, l, p]
    [t_arr, X_arr, Y1_arr, Z1_arr] = approx_system_i(init_conds_i, params_i, t_i)
    l0_X.set_ydata(X_arr)
    l0_X.set_xdata(t_arr)
    l0_Y1.set_ydata(Y1_arr)
    l0_Y1.set_xdata(t_arr)
    l0_Z1.set_ydata(Z1_arr)
    l0_Z1.set_xdata(t_arr)
    ax[0].set_xlim(0, t_i)
    max_elt = 1.1 * max([np.max(X_arr), np.max(Y1_arr), np.max(Z1_arr)])
    ax[0].set_ylim(0, max_elt)

    X = X_arr[-1]
    Y1 = Y1_arr[-1]
    Z1 = Z1_arr[-1]
    init_conds_f = [X, Y1, Y2, Z1]
    params_f = [b1, b2, g, d, a, l, p]
    [t_arr, X_arr, Y1_arr, Y2_arr, Z1_arr, Z2_arr] = approx_system_f(init_conds_f, params_f, t_i, t_f)
    l1_X.set_ydata(X_arr)
    l1_X.set_xdata(t_arr)
    l1_Y1.set_ydata(Y1_arr)
    l1_Y1.set_xdata(t_arr)
    l1_Y2.set_ydata(Y2_arr)
    l1_Y2.set_xdata(t_arr)
    l1_Z1.set_ydata(Z1_arr)
    l1_Z1.set_xdata(t_arr)
    l1_Z2.set_ydata(Z2_arr)
    l1_Z2.set_xdata(t_arr)
    ax[1].set_xlim(t_i, t_f)
    max_elt = 1.1 * max([np.max(X_arr), np.max(Y1_arr), np.max(Y2_arr), np.max(Z1_arr), np.max(Z2_arr)])
    ax[1].set_ylim(0, max_elt)

    # for plot in plots:
    #     plot.set_xdata(t)

    fig.canvas.draw_idle()

for slider in sliders:
    slider.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

# rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


# def colorfunc(label):
#     l.set_color(label)
#     fig.canvas.draw_idle()
# radio.on_clicked(colorfunc)

plt.show()