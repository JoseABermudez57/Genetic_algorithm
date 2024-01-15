from fractions import Fraction
import pandas as pd
from operations import genetic_algorithm as ga
import matplotlib.pyplot as plt


def start_simulation(data):
    statistics_by_iteration = []
    a = int(data["a"])
    b = int(data["b"])
    pob_min = int(data["pob_min"])
    prob_mut_individual = float(data["prob_mut_individual"])
    prob_mut_gene = float(data["prob_mut_gene"])
    res = float(Fraction(data["res"]))
    iterations = int(data["iterations"])
    pob_max = int(data["pob_max"])
    max_or_min = data["max_or_min"].get()

    qt_bits, delta_x = ga.gen_base_values(a, b, res)
    ga.gen_individuals(pob_min, qt_bits, a, delta_x)

    for _ in range(iterations):
        couples = ga.generate_couples(ga.data.get('Individuo'), 4)
        children = ga.crossover_pairs(couples)
        ga.mutate_pob(children, prob_mut_individual, prob_mut_gene, delta_x, a)
        statistics_by_iteration.append(ga.maximus_and_minimus(max_or_min))

    df = pd.DataFrame(ga.data)
    df.to_csv('estadisticos.csv')

    ga.pruning(max_or_min, pob_max)

    print(ga.data)

    iterations_for_graphic = list(range(1, len(statistics_by_iteration) + 1))  # Número de iteraciones

    best_values = [elem[0] for elem in statistics_by_iteration]
    worst_values = [elem[1] for elem in statistics_by_iteration]
    prom_values = [elem[2] for elem in statistics_by_iteration]

    plt.figure(figsize=(10, 6))

    plt.plot(iterations_for_graphic, best_values, label='Mejores resultados', marker='^', linestyle='-')

    plt.plot(iterations_for_graphic, worst_values, label='Peores resultados', marker='s', linestyle='--', color='orange')

    plt.plot(iterations_for_graphic, prom_values, label='Promedio', marker='o', linestyle='-.', color='green')

    for i, txt in enumerate(statistics_by_iteration):
        plt.text(iterations_for_graphic[i], best_values[i], f'{round(best_values[i], 2):.2f}', ha='right', va='bottom')
        plt.text(iterations_for_graphic[i], worst_values[i], f'{round(worst_values[i],2):.2f}', ha='left', va='bottom')
        plt.text(iterations_for_graphic[i], prom_values[i], f'{round(prom_values[i], 2):.2f}', ha='right', va='top')

    plt.title('Valores a lo largo de las Iteraciones')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()
