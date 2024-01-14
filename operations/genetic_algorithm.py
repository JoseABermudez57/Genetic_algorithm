import math
import random

import pandas as pd

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


gen_individuals(4, 31, 5, 3, (2/31))
df = pd.DataFrame(data)
df.index = df.index + 1
print(df)
print(data['Individuo'])


def generate_couples(binary_list, n):
    couples = []

    for individual in binary_list:
        m = random.randint(0, n)
        couple_individuals = random.sample(binary_list, m)

        if individual in couple_individuals:
            couple_individuals.remove(individual)

        couples.append((individual, couple_individuals))

    return couples


pairs = generate_couples(data.get('Individuo'), len(data))


def crossover_pairs(pairs_of_individuals):

    child_of_cross = []

    for fs_part_pair, sn_part_pair in pairs_of_individuals:
        for part_pair in sn_part_pair:

            crossover_point = random.randint(0, len(fs_part_pair) - 1)
            print(crossover_point)

            frst_pair_first_part = fs_part_pair[:crossover_point]
            frst_pair_second_part = fs_part_pair[crossover_point:]

            scn_pair_first_part = part_pair[:crossover_point]
            scn_pair_second_part = part_pair[crossover_point:]

            frst_children = frst_pair_first_part + scn_pair_second_part
            scn_children = scn_pair_first_part + frst_pair_second_part

            child_of_cross.append(frst_children)
            child_of_cross.append(scn_children)

    return child_of_cross


children = crossover_pairs(pairs)
def mutate_children(children_list, prob_individual_mutation, prob_gen_mutation):

    find_individual_mutation_rate = [
        round(random.random(), 2) for _ in range(len(children_list))
    ]

    children_and_prob_individual_mutation_rate = tuple(zip(children_list, find_individual_mutation_rate))

    print(children_and_prob_individual_mutation_rate)

    find_gen_mutation_rate = [
        child_and_prob[0] for child_and_prob in children_and_prob_individual_mutation_rate
        if child_and_prob[1] <= prob_individual_mutation
    ]

    return gen_mutation_children(find_gen_mutation_rate, prob_gen_mutation)


def gen_mutation_children(fnd_mutation_rate, prob_gen_mutation):
    mutations = []

    for binary_string in fnd_mutation_rate:
        new_individual = ''
        for bit in binary_string:
            random_number = round(random.random(), 2)

            if random_number <= prob_gen_mutation:
                new_bit = 1 - int(bit)
            else:
                new_bit = int(bit)

            new_individual += str(new_bit)

        mutations.append(new_individual)

    return mutations


mutate_children(children, 0.6, 0.5)
