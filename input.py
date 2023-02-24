from project import Project
import random
N = 20
n = 8
def gen_random_projects():
    all_cords = []
    projects = []
    while len(all_cords) != N:
        f1 = round(random.uniform(0,2*n),2)
        f2 = round(random.uniform(0,2*n),2)
        if (f1 - n)**2 + (f2 - n)**2 <= n**2 and\
            -f1 + f2 <= n and\
            f1 + f2 >= 2*n:
            cords = (f1,f2)
            if(any(all_cords) != cords):
                all_cords.append(cords)
                project = Project(cords[0],cords[1])
                projects.append(project)
    return projects


