from project import Project
import random
N = 20
n = 8

def cords_exist(all_cords,cords):
    for i in range(len(all_cords)):
        if(all_cords[i][0] == cords[0] and all_cords[i][1] == cords[1]):
           return True
    return False

def gen_random_projects():
    all_cords = []
    projects = []
    i = 1
    while len(all_cords) != N:
        f1 = round(random.uniform(0,2*n),2)
        f2 = round(random.uniform(0,2*n),2)
        if (f1 - n)**2 + (f2 - n)**2 <= n**2 and\
            -f1 + f2 <= n and\
            f1 + f2 >= 2*n:
            cords = (f1,f2)
            if not cords_exist(all_cords,cords):
                all_cords.append(cords)
                project = Project(cords[0],cords[1],i)
                projects.append(project)
                i += 1
    return projects

def gen_projects():
    all_cords = []
    projects = []
    i = 1
    while len(all_cords) != N:
        print(i," = ",end="")
        f1,f2 = input().split()
        f1 = round(float(f1),2)
        f2 = round(float(f2),2)
        if (f1 - n)**2 + (f2 - n)**2 <= n**2 and\
            -f1 + f2 <= n and\
            f1 + f2 >= 2*n:
            cords = (f1,f2)
            if not cords_exist(all_cords, cords):
                all_cords.append(cords)
                project = Project(cords[0],cords[1],i)
                projects.append(project)
                i += 1
            else:
                print("Введенная точка уже существует!")
        else:
            print("Введенная точка не входит в границы заданной области!")
    return projects


