from tables import *
from graphics import draw_graphics

if __name__ == '__main__':
    project_data = gen_random_projects()
    print("Таблица исключения:")
    draw_exclude_table(project_data)
    print("Множество Парето:")
    pareto = make_pareto(project_data)
    show_pareto(pareto)
    print("Таблица кластеризации:")
    draw_cluster_table(project_data)
    draw_graphics(project_data,pareto)






