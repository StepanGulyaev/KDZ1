from tables import *


if __name__ == '__main__':
    project_data = gen_random_projects()
    draw_exclude_table(project_data)
    show_pareto(make_pareto(project_data))





