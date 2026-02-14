import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation
import random

def figure():
    #creating points for our graph
    t = np.linspace(1,10,500)

    #create our canvas
    fig, axis = plt.subplots()
    plot, = axis.plot([],[])
    fig.canvas.manager.set_window_title('Lissage figures')

    #set the limits of the graph
    axis.set_xlim([-5,5])
    axis.set_ylim([-5,5])
    
    a = 0
    b = 0

    #
    def update(frame):
        global a,b 

        if frame == 0: 
            a = random.randint(1,5)
            b = random.randint(1,5)
            plt.title(f"Lissage figure with a = {a} and b = {b}")
            
        delta = (np.pi / 2) + frame * 0.05
        x = a*np.sin(a*t+delta)
        y = b*np.sin(b*t)
        plot.set_data(x[:frame], y[:frame])
        return plot
    
    
    animation = FuncAnimation(fig=fig, func=update, frames=len(t), interval=10, repeat=True)
    plt.show()

#starts main function    
figure()