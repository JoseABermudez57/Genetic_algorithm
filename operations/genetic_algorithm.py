import math
import random

data = {
    'Individuo': [],
    'i': [],
    'x': [],
    'f(x)': []
}


def gen_base_values(a, b, bits_length, delta_x_tch):
    ranges = b - a
    jumps_tch = ranges / delta_x_tch
    points_tch = jumps_tch + 1
    qt_bits_tch = math.ceil(math.log(points_tch, 2))
    print(delta_x_tch, points_tch, jumps_tch)
    if 2 ** (qt_bits_tch - 1) < points_tch <= 2 ** qt_bits_tch:
        print("correcto", qt_bits_tch)
    else:
        print("incorrecto", qt_bits_tch)

    print("_______________________")

    delta_x = ranges / (pow(2, bits_length) - 1)
    jumps = ranges / delta_x
    points = jumps + 1
    qt_bits = math.ceil(math.log(points, 2))
    print(delta_x, points, jumps)
    if 2 ** (qt_bits - 1) < points <= 2 ** qt_bits:
        print("correcto", qt_bits)
    else:
        print("incorrecto", qt_bits)


def gen_individuals(min_population, jumps, qt_bits, a, delta_x):
    random_nums = [random.randint(0, jumps) for _ in range(min_population)]
    binary_nums = [format(int(num), f'0{qt_bits}b') for num in random_nums]
    x_values = [round(a + i * delta_x, 4) for i in random_nums]
    fx_values = [round((i**3 - 2 * (i**2) * math.cos(math.radians(i)) + 3), 4) for i in x_values]

    data['Individuo'].extend(binary_nums)
    data['i'].extend(random_nums)
    data['x'].extend(x_values)
    data['f(x)'].extend(fx_values)
