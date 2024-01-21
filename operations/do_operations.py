from fractions import Fraction
import pandas as pd
from operations import genetic_algorithm as ga
import matplotlib.pyplot as plt
import imageio
import os
import numpy as np


def start_simulation(data):
    statistics_by_iteration = []
    statistics_by_generation = []
    a = int(data["a"])
    b = int(data["b"])
    pob_min = int(data["pob_min"])
    prob_mut_individual = float(data["prob_mut_individual"])
    prob_mut_gene = float(data["prob_mut_gene"])
    res = float(Fraction(data["res"]))
    iterations = int(data["iterations"])
    pob_max = int(data["pob_max"])
    max_or_min = data["max_or_min"]

    qt_bits, delta_x = ga.gen_base_values(a, b, res)
    ga.gen_individuals(pob_min, qt_bits, a, delta_x)

    for i in range(iterations):
        couples = ga.generate_couples(ga.data.get('Individuo'), 4)
        children = ga.crossover_pairs(couples)
        mutate_pob = ga.mutate_pob(children, prob_mut_individual, prob_mut_gene, delta_x, a)
        statistics_by_generation.append(mutate_pob)
        statistics_by_iteration.append(ga.maximus_and_minimus(max_or_min))
        ga.pruning(max_or_min, pob_max)

    output_csv_folder = "Estadisticos"
    os.makedirs(output_csv_folder, exist_ok=True)
    df = pd.DataFrame(ga.data)
    df.to_csv(f'{output_csv_folder}/estadisticos.csv')

    show_statistics_by_iteration_graphic(statistics_by_iteration)
    show_statistics_by_generation_graphic(statistics_by_generation, a, b)
    print("PNG's hechos!")
    make_gif_from_graphics()


def custom_function(x):
    return x ** 3 - (x ** 3) * np.cos(x * 5.0)


def show_statistics_by_iteration_graphic(statistics_by_iteration):
    output_folder = 'gráficas_individuales/iteraciones/'
    os.makedirs(output_folder, exist_ok=True)

    iterations_for_graphic = list(range(1, len(statistics_by_iteration) + 1))

    best_values_iteration = [elem[0] for elem in statistics_by_iteration]
    worst_values_iteration = [elem[1] for elem in statistics_by_iteration]
    avg_values_iteration = [elem[2] for elem in statistics_by_iteration]

    plt.figure(figsize=(10, 6))

    plt.plot(iterations_for_graphic, best_values_iteration, label='Mejores resultados', marker='^', linestyle='-')
    plt.plot(iterations_for_graphic, worst_values_iteration, label='Peores resultados', marker='s', linestyle='--',
             color='orange')
    plt.plot(iterations_for_graphic, avg_values_iteration, label='Promedio', marker='o', linestyle='-.', color='green')

    plt.title('Valores a lo largo de las Iteraciones')
    plt.xlabel('Iteración')
    plt.ylabel('Fitness')
    plt.legend()
    plt.grid(True)
    filename = os.path.join(output_folder, 'Grafica_estadisticos.png')
    plt.savefig(filename)
    plt.close()


def show_statistics_by_generation_graphic(statistics_by_generation, a, b):

    num_points = 1000
    output_folder = 'gráficas_individuales/generaciones/'
    os.makedirs(output_folder, exist_ok=True)

    for i, lista in enumerate(statistics_by_generation):
        if not lista:
            continue

        plt.figure()

        x_range = np.linspace(a, b, num_points)
        y_range = custom_function(x_range)
        plt.plot(x_range, y_range, label=r'Función', color='black', linestyle='--')

        x_values = [point[1] for point in lista]
        y_values = [point[0] for point in lista]

        idx_max = np.argmax(y_values)
        idx_min = np.argmin(y_values)

        plt.scatter(x_values, y_values, label=f'Demás individuos {i + 1}')

        plt.scatter(x_values[idx_max], y_values[idx_max], color='green', label='Valor Máximo')
        plt.scatter(x_values[idx_min], y_values[idx_min], color='red', label='Valor Mínimo')

        plt.xlim(a, b)

        plt.title(f'Generación {i + 1}')
        plt.xlabel('Rango')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)

        filename = os.path.join(output_folder, f'Grafica_generacion_{i + 1}.png')
        plt.savefig(filename)
        plt.close('all')


def make_gif_from_graphics():

    input_folder = 'gráficas_individuales/generaciones/'
    output_folder = 'gráficas_individuales/gif/'
    os.makedirs(output_folder, exist_ok=True)

    file_names = sorted(
        [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png')])

    output_gif = 'gráficas_individuales/gif/generaciones.gif'

    images = [imageio.imread(file) for file in file_names]
    imageio.mimsave(output_gif, images, duration=3)

    print(f'GIF guardado en: {output_gif}')
