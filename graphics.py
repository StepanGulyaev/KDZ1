import numpy as np
import matplotlib.pyplot as plt
from tables import *


def draw_graphics(project_data,pareto):
    ax = plt.gca()
    ax.cla()

    major_ticks = np.arange(0, 17, 2)
    minor_ticks = np.arange(0, 17,1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # And a corresponding grid
    ax.grid(which='both')

    ax.set_title('(f1 - 8)² + (f2 -8 )² ≤ 64; -f1 + f2 ≤ 8; f1 + f2 ≥ 16',)
    ax.set_aspect(1)
    ax.set_xlim((0, 16))
    ax.set_ylim((0, 16))
    circle = plt.Circle((8, 8), 8, color='b', fill=False)
    f1 = np.arange(0, 16, 0.01)
    ax.plot(f1, f1 + n, f1, -f1 + 2 * n)
    ax.add_patch(circle)
    plt.xlabel(r'$f1$')
    plt.ylabel(r'$f2$')
    plt.grid(True)



    for i in range(len(project_data)):
        if project_data[i] not in pareto:
            ax.plot(project_data[i].f1,project_data[i].f2,'k.')
        else:
            ax.plot(project_data[i].f1, project_data[i].f2,'r.')
        ax.annotate(str(i+1),xy=(project_data[i].f1,project_data[i].f2),xytext=(project_data[i].f1 - 0.3 ,project_data[i].f2 + 0.3))
    plt.show()



