from fractions import Fraction
import pandas as pd
from operations import genetic_algorithm as ga
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np


def start_simulation(data):
    statistics_by_iteration = []
    statistics_by_generation = []
    a = int(data["a"])
    b = int(data["b"])
    pob_min = int(data["pob_min"])
    pob_max = int(data["pob_max"])
    prob_mut_individual = float(data["prob_mut_individual"])
    prob_mut_gene = float(data["prob_mut_gene"])
    res = float(Fraction(data["res"]))
    iterations = int(data["iterations"])
    max_or_min = data["max_or_min"]

    qt_bits, delta_x = ga.gen_base_values(a, b, res)
    ga.gen_individuals(pob_min, qt_bits, a, delta_x)

    for i in range(iterations):
        # Generate couples
        couples = ga.generate_couples(ga.data.get('Individuo'), 4)

        # Generate children
        children = ga.crossover_pairs(couples)

        # Generate mutate children and add they to the population
        ga.mutate_pob(children, prob_mut_individual, prob_mut_gene, delta_x, a)

        # Save statistic data for graphic #1
        statistics_by_iteration.append(ga.maximus_and_minimus(max_or_min))

        # Save population by generation for graphic #2
        statistics_by_generation.append(list(zip(ga.data['x'], ga.data['f(x)'])))

        # Pruning
        ga.pruning(max_or_min, pob_max)

    # Create folder to store statistical data (population and best, worst and average value)
    output_csv_folder = "Estadisticos"

    os.makedirs(output_csv_folder, exist_ok=True)
    df = pd.DataFrame(ga.data)
    df.to_csv(f'{output_csv_folder}/Poblacion.csv')

    best, worst, average_evaluated = ga.maximus_and_minimus(max_or_min)

    df = pd.DataFrame({
        'Mejor': [best],
        'peor': [worst],
        'Promedio': [average_evaluated],
    })

    df.to_csv(f'{output_csv_folder}/Estadisticos.csv')

    # Graph generation process
    show_statistics_by_generation_graphic(statistics_by_iteration)
    show_generations_graphic(statistics_by_generation, a, b, max_or_min)
    print("PNG's hechos!")
    make_video_from_graphics()


def show_statistics_by_generation_graphic(statistics_by_iteration):
    output_folder = 'graficas_individuales/iteraciones/'
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

    plt.title('Evolución a lo largo de las generaciones')
    plt.xlabel('Generación')
    plt.ylabel('Fitness')
    plt.legend()
    plt.grid(True)
    filename = os.path.join(output_folder, 'Grafica_estadisticos.png')
    plt.savefig(filename)
    plt.close('all')


def show_generations_graphic(statistics_by_generation, a, b, max_or_min):
    num_points = 100
    output_folder = 'graficas_individuales/generaciones/'
    os.makedirs(output_folder, exist_ok=True)

    for i, generation_data in enumerate(statistics_by_generation):

        x_range = np.linspace(a, b, num_points)
        y_range = ga.fx_value(x_range)

        fig, ax = plt.subplots()

        ax.plot(x_range, y_range, label='Función', color='black', linestyle='--')

        x_values = [point[0] for point in generation_data]
        y_values = [point[1] for point in generation_data]

        idx_max = np.argmax(y_values)
        idx_min = np.argmin(y_values)

        ax.scatter(x_values, y_values, label=f'Demás individuos')

        if max_or_min:
            ax.scatter(x_values[idx_max], y_values[idx_max], color='red', label='Peor individuo')
            ax.scatter(x_values[idx_min], y_values[idx_min], color='green', label='Mejor individuo')
        else:
            ax.scatter(x_values[idx_max], y_values[idx_max], color='green', label='Mejor individuo')
            ax.scatter(x_values[idx_min], y_values[idx_min], color='red', label='Peor individuo')

        ax.set_xlim(a, b)

        ax.set_title(f'Generación {i + 1}')
        ax.set_xlabel('Rango')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)

        filename = os.path.join(output_folder, f'Grafica_generacion_{i + 1}.png')
        plt.savefig(filename)
        print("Lista hecha: ", filename)
        ax.clear()
        plt.close()


def make_video_from_graphics():
    input_folder = 'graficas_individuales/generaciones/'
    output_folder = 'graficas_individuales/video/'
    os.makedirs(output_folder, exist_ok=True)

    file_names = sorted(
        [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png')],
        key=lambda x: int(x.split('_generacion_')[1].split('.png')[0])
    )

    output_video = 'graficas_individuales/video/generaciones.mp4'

    first_image = cv2.imread(file_names[0])
    height, width, layers = first_image.shape

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"mp4v"), 3, (width, height), True)

    for file in file_names:
        img = cv2.imread(file)
        video.write(img)

    video.release()

    print(f'Video guardado en: {output_video}')
