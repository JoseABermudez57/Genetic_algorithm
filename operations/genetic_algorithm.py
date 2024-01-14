import math
import random


class GeneticAlgorithm:
    def __init__(self, a, b, bits_length, delta_x_tch, min_population, jumps):
        self.a = a
        self.b = b
        self.bits_length = bits_length
        self.delta_x_tch = delta_x_tch
        self.min_population = min_population
        self.jumps = jumps
        self.data = {
            'Individuo': [],
            'i': [],
            'x': [],
            'f(x)': []
        }

    def gen_base_values(self):
        ranges = self.b - self.a
        jumps_tch = ranges / self.delta_x_tch
        points_tch = jumps_tch + 1
        qt_bits_tch = math.ceil(math.log(points_tch, 2))
        if 2 ** (qt_bits_tch - 1) < points_tch <= 2 ** qt_bits_tch:
            print("correcto", qt_bits_tch)
        else:
            print("incorrecto", qt_bits_tch)

        delta_x = ranges / (pow(2, self.bits_length) - 1)
        jumps = ranges / delta_x
        points = jumps + 1
        qt_bits = math.ceil(math.log(points, 2))
        if 2 ** (qt_bits - 1) < points <= 2 ** qt_bits:
            print("correcto", qt_bits)
        else:
            print("incorrecto", qt_bits)

    def gen_individuals(self):
        random_nums = [random.randint(0, self.jumps) for _ in range(self.min_population)]
        binary_nums = [format(int(num), f'0{self.bits_length}b') for num in random_nums]
        x_values = [round(self.a + i * self.delta_x_tch, 4) for i in random_nums]
        fx_values = [round((i**3 - 2 * (i**2) * math.cos(math.radians(i)) + 3), 4) for i in x_values]

        self.data['Individuo'].extend(binary_nums)
        self.data['i'].extend(random_nums)
        self.data['x'].extend(x_values)
        self.data['f(x)'].extend(fx_values)
