import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

NUM_STEPS = 1000

def approx_system(init_conds, params):
    [X_0, Y1_0, Y2_0] = init_conds

    Z1_0 = 0
    Z2_0 = 0

    [b1, b2, g, d, a, l, p] = params

    t_0 = 0
    t_f = 10
    dt = (t_f - t_0) / NUM_STEPS

    # N = X + Y1 + Y2 + Z1 + Z2

    t_arr = np.linspace(t_0, t_f, NUM_STEPS+1)
    X_arr = np.ones(NUM_STEPS+1)*X_0
    Y1_arr = np.ones(NUM_STEPS+1)*Y1_0
    Y2_arr = np.ones(NUM_STEPS+1)*Y2_0
    Z1_arr = np.ones(NUM_STEPS+1)*Z1_0
    Z2_arr = np.ones(NUM_STEPS+1)*Z2_0

    for i in range(NUM_STEPS):
        X = X_arr[i]
        Y1 = Y1_arr[i]
        Y2 = Y2_arr[i]
        Z1 = Z1_arr[i]
        Z2 = Z2_arr[i]
        X_arr[i+1] = X + dt * (-b1*X*Y1 - b2*X*Y2 + p*l*Z1 + p*l*Z2)
        Y1_arr[i+1] = Y1 + dt * (b1*X*Y1 - g*Y1 + d*b1*Y1*Z1 + (1-p)*a*b1*Y1*Z2)
        Y2_arr[i+1] = Y2 + dt * (b2*X*Y2 - g*Y2 + d*b2*Y2*Z2 + (1-p)*a*b2*Y2*Z1)
        Z1_arr[i+1] = Z1 + dt * (g*Y1 - d*b1*Y1*Z1 - p*l*Z1 - (1-p)*a*b2*Y2*Z1)
        Z2_arr[i+1] = Z2 + dt * (g*Y2 - d*b2*Y2*Z2 - p*l*Z1 - (1-p)*a*b1*Y1*Z2)
        # print(i, f"{Z1:.1f}", f"{Y1:.1f}", X, f"{Y2:.1f}", f"{Z2:.1f}", sep='\t')

    values = np.array([t_arr, X_arr, Y1_arr, Y2_arr, Z1_arr, Z2_arr])

    return values

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.6)
def_X = 10
def_Y1 = 1
def_Y2 = 1
def_init_conds = [def_X, def_Y1, def_Y2]
def_b1 = 1.0
def_b2 = 1.0
def_g = 1.0
def_d = 1.0
def_a = 1.0
def_l = 1.0
def_p = 0.5
def_params = [def_b1, def_b2, def_g, def_d, def_a, def_l, def_p]
[t, X, Y1, Y2, Z1, Z2] = approx_system(def_init_conds, def_params)
l_X, = plt.plot(t, X, lw=2, label="$X$")
l_Y1, = plt.plot(t, Y1, lw=2, label="$Y1$")
l_Y2, = plt.plot(t, Y2, lw=2, label="$Y2$")
l_Z1, = plt.plot(t, Z1, lw=2, label="$Z1$")
l_Z2, = plt.plot(t, Z2, lw=2, label="$Z2$")
plt.legend()
# plt.axis([t[0], t[-1], -10, 10])

axcolor = 'lightgoldenrodyellow'
ax_X = plt.axes([0.25, 0.45, 0.65, 0.03], facecolor=axcolor)
ax_Y1 = plt.axes([0.25, 0.5, 0.65, 0.03], facecolor=axcolor)
ax_Y2 = plt.axes([0.25, 0.55, 0.65, 0.03], facecolor=axcolor)
ax_b1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_b2= plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_g = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_a = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=axcolor)
ax_l = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)
ax_p = plt.axes([0.25, 0.4, 0.65, 0.03], facecolor=axcolor)
# ax_alpha2 = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)

valmin = 0.0
param_max = 5.0
init_cond_max = 10.0
random_max = 1
s_X = Slider(ax_X, '$X$', valmin, init_cond_max, valinit=def_X)
s_Y1 = Slider(ax_Y1, '$Y1$', valmin, init_cond_max, valinit=def_Y1)
s_Y2 = Slider(ax_Y2, '$Y2$', valmin, init_cond_max, valinit=def_Y2)
s_b1 = Slider(ax_b1, '$\\beta1$', valmin, param_max, valinit=def_b1)
s_b2 = Slider(ax_b2, '$\\beta2$', valmin, param_max, valinit=def_b2)
s_g = Slider(ax_g, '$\\gamma$', valmin, param_max, valinit=def_g)
s_d = Slider(ax_d, '$\\delta$', valmin, param_max, valinit=def_d)
s_a = Slider(ax_a, '$\\alpha$', valmin, param_max, valinit=def_a)
s_l = Slider(ax_l, '$\\lambda$', valmin, param_max, valinit=def_l)
s_p = Slider(ax_p, '$\\rho$', valmin, random_max, valinit=def_p)
# salpha2 = Slider(ax_alpha2, '$\\alpha2$', valmin, param_max, valinit=def_alpha2)
sliders = [s_X, s_Y1, s_Y2, s_b1, s_b2, s_g, s_d, s_a, s_l, s_p]

def update(val):
    X = s_X.val
    Y1 = s_Y1.val
    Y2 = s_Y2.val
    init_conds = [X, Y1, Y2]
    b1 = s_b1.val
    b2 = s_b2.val
    g = s_g.val
    d = s_d.val
    a = s_a.val
    l = s_l.val
    p = s_p.val
    # alpha2 = s_alpha2.val
    params = [b1, b2, g, d, a, l, p]
    [t, X, Y1, Y2, Z1, Z2] = approx_system(init_conds, params)
    l_X.set_ydata(X)
    l_Y1.set_ydata(Y1)
    l_Y2.set_ydata(Y2)
    l_Z1.set_ydata(Z1)
    l_Z2.set_ydata(Z2)
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