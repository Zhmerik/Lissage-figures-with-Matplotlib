import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np
import random 

# Make data
t = np.linspace(1,10,500)

a = 0
b = 0 
c = 0

fig, ax = plt.subplots(
    figsize = (8,8),
    subplot_kw={"projection": "3d"}    
)

fig.canvas.manager.set_window_title('Lissage figures 3d')
ax.set_xlim(-7,7)
ax.set_ylim(-7,7)
ax.set_zlim(-7,7)

plot, = ax.plot([],[],[])

def update(frame):
    global a,b,c

    if frame == 0:
        a = random.randint(-5,5)
        b = random.randint(-5,5)
        c = random.randint(-5,5)

    delta = (np.pi / 2) + frame * 0.05
    x = a*np.sin(a*t+delta)
    y = b*np.sin(b*t)
    z = c*np.sin(c*t)

    plt.title(f"3D Lissage figure with a = {a} b = {b} and c = {c}")

    plot.set_data(x[:frame],y[:frame])
    plot.set_3d_properties(z[:frame])
    return plot


animation = FuncAnimation(fig=fig,func=update, frames=len(t), interval= 20, repeat=True)

def close(event):
    try:
        animation.event_source.stop()
    except AttributeError:
        pass
    exit()
    
fig.canvas.mpl_connect('close_event', close)

plt.show()