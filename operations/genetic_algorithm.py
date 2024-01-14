import math
import random

data = {
    'Individuo': [],
    'i': [],
    'x': [],
    'f(x)': []
}


def gen_base_values(a, b, bits_length, delta_x_tch):
    graphic_range = b - a

    delta_x = delta_x_evaluation(graphic_range, bits_length, delta_x_tch)

    jumps = graphic_range / delta_x
    points = jumps + 1
    qt_bits = math.ceil(math.log(points, 2))
    print(delta_x, points, jumps)
    if 2 ** (qt_bits - 1) < points <= 2 ** qt_bits:
        print("correcto", qt_bits)
    else:
        print("incorrecto", qt_bits)


def delta_x_evaluation(graphic_range, qt_bits, delta_x_tch):
    delta_x = graphic_range / (pow(2, qt_bits) - 1)
    if delta_x_tch > delta_x:
        return delta_x
    else:
        return delta_x_tch


def gen_individuals(min_population, jumps, qt_bits, a, delta_x):
    random_nums = [random.randint(0, jumps) for _ in range(min_population)]
    binary_nums = [format(int(num), f'0{qt_bits}b') for num in random_nums]
    x_values = [round(a + i * delta_x, 4) for i in random_nums]
    fx_values = [round((i**3 - 2 * (i**2) * math.cos(math.radians(i)) + 3), 4) for i in x_values]

    data['Individuo'].extend(binary_nums)
    data['i'].extend(random_nums)
    data['x'].extend(x_values)
    data['f(x)'].extend(fx_values)


def generate_couples(binary_list, n):
    couples = []

    for individual in binary_list:
        m = random.randint(0, n)
        couple_individuals = random.sample(binary_list, m)

        if individual in couple_individuals:
            couple_individuals.remove(individual)

        couples.append((individual, couple_individuals))

    return couples

