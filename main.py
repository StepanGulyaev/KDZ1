from tables import *
from graphics import draw_pareto_projects
from graphics import draw_cluster_projects

if __name__ == '__main__':
    option = ""
    while option != "1" and option != "2":
        print("Введите 1 для ручного ввода информации о проектах, 2 для случайной генерации данных: ",end = "")
        option = input()
        if(option == "1"):
            print("Будет введено",N,"точек")
            project_data = gen_projects()
        elif(option == "2"):
            project_data = gen_random_projects()
        else:
            print("Некорректная опция!")
    print("Таблица исключения:")
    draw_exclude_table(project_data)
    print("Множество Парето:")
    pareto = make_pareto(project_data)
    show_pareto(pareto)
    print("Таблица кластеризации:")
    draw_cluster_table(project_data)
    draw_pareto_projects(project_data,pareto)
    draw_cluster_projects(project_data)







