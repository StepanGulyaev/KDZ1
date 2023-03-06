import numpy as np
import matplotlib.pyplot as plt
from tables import *


def draw_field(field):
    major_ticks = np.arange(0, 17, 2)
    minor_ticks = np.arange(0, 17,1)

    field.set_xticks(major_ticks)
    field.set_xticks(minor_ticks, minor=True)
    field.set_yticks(major_ticks)
    field.set_yticks(minor_ticks, minor=True)

    # And a corresponding grid
    field.grid(which='both')

    field.set_title('(f1 - 8)² + (f2 -8 )² ≤ 64; -f1 + f2 ≤ 8; f1 + f2 ≥ 16',)
    field.set_aspect(1)
    field.set_xlim((0, 16))
    field.set_ylim((0, 16))
    circle = plt.Circle((8, 8), 8, color='b', fill=False)
    f1 = np.arange(0, 16, 0.01)
    field.plot(f1, f1 + n, f1, -f1 + 2 * n)
    field.add_patch(circle)
    plt.xlabel(r'$f1$')
    plt.ylabel(r'$f2$')
    plt.grid(True)


def draw_pareto_projects(project_data,pareto):
    field = plt.gca()
    draw_field(field)
    for i in range(len(project_data)):
        if project_data[i] not in pareto:
            field.plot(project_data[i].f1,project_data[i].f2,'k.')
        else:
            field.plot(project_data[i].f1, project_data[i].f2,'r.')
        field.annotate(str(i+1),xy=(project_data[i].f1,project_data[i].f2),xytext=(project_data[i].f1 - 0.5 ,project_data[i].f2 - 0.65))
    plt.show()

def draw_cluster_projects(project_data):
    field = plt.gca()
    draw_field(field)
    for i in range(len(project_data)):
        if project_data[i].cluster == 1:
            field.plot(project_data[i].f1,project_data[i].f2,'r.')
        elif project_data[i].cluster == 2:
            field.plot(project_data[i].f1, project_data[i].f2,'g.')
        elif project_data[i].cluster == 3:
            field.plot(project_data[i].f1, project_data[i].f2, 'b.')
        field.annotate(str(i+1),xy=(project_data[i].f1,project_data[i].f2),xytext=(project_data[i].f1 - 0.5 ,project_data[i].f2 - 0.65))
    plt.show()




