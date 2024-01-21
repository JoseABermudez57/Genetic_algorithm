import math
import random

data = {
    'Individuo': [],
    'i': [],
    'x': [],
    'f(x)': []
}


def gen_base_values(a, b, delta_x_tch):
    graphic_range = abs(b - a)
    jumps = graphic_range / delta_x_tch
    points = jumps + 1
    qt_bits = math.ceil(math.log(points, 2))

    delta_x = delta_x_evaluation(graphic_range, qt_bits, delta_x_tch)

    return qt_bits, delta_x


def delta_x_evaluation(graphic_range, qt_bits, delta_x_tch):
    delta_x = graphic_range / (pow(2, qt_bits) - 1)
    if delta_x_tch > delta_x:
        return delta_x
    else:
        return delta_x_tch


def gen_individuals(min_population, qt_bits, a, delta_x):

    random_nums = random.sample(range((pow(2, qt_bits))), min_population)
    binary_nums = [format(int(num), f'0{qt_bits}b') for num in random_nums]
    x_values = [x_value(a, i, delta_x) for i in random_nums]
    fx_values = [fx_value(i) for i in x_values]

    data['Individuo'].extend(binary_nums)
    data['i'].extend(random_nums)
    data['x'].extend(x_values)
    data['f(x)'].extend(fx_values)


def x_value(a, i, delta_x):
    return round(a + i * delta_x, 4)


def i_value(individual):
    return int(individual, 2)


def fx_value(i):
    return round(i**3 - (i**3) * math.cos(i * 5), 4)


def generate_couples(binary_list, n):
    couples = []

    for individual in binary_list:
        m = random.randint(0, n)
        couple_individuals = random.sample(binary_list, m)

        if individual in couple_individuals:
            couple_individuals.remove(individual)

        couples.append((individual, couple_individuals))

    return couples


def crossover_pairs(pairs_of_individuals):

    child_of_cross = []

    for fs_part_pair, sn_part_pair in pairs_of_individuals:
        for part_pair in sn_part_pair:

            crossover_point = random.randint(0, len(fs_part_pair) - 1)

            frst_pair_first_part = fs_part_pair[:crossover_point]
            frst_pair_second_part = fs_part_pair[crossover_point:]

            scn_pair_first_part = part_pair[:crossover_point]
            scn_pair_second_part = part_pair[crossover_point:]

            frst_children = frst_pair_first_part + scn_pair_second_part
            scn_children = scn_pair_first_part + frst_pair_second_part

            child_of_cross.append(frst_children)
            child_of_cross.append(scn_children)

    return child_of_cross


def mutate_pob(children_list, prob_individual_mutation, prob_gen_mutation, delta_x, a):

    find_individual_mutation_rate = [
        round(random.random(), 2) for _ in range(len(children_list))
    ]

    children_and_prob_individual_mutation_rate = tuple(zip(children_list, find_individual_mutation_rate))

    find_gen_mutation_rate = [
        child_and_prob[0] for child_and_prob in children_and_prob_individual_mutation_rate
        if child_and_prob[1] <= prob_individual_mutation
    ]

    return gen_mutation_children(find_gen_mutation_rate, prob_gen_mutation, delta_x, a)


def gen_mutation_children(fnd_mutation_rate, prob_gen_mutation, delta_x, a):
    generations = []

    for binary_string in fnd_mutation_rate:
        new_individual = ''
        for bit in binary_string:
            random_number = round(random.random(), 2)

            if random_number <= prob_gen_mutation:
                new_bit = 1 - int(bit)
            else:
                new_bit = int(bit)

            new_individual += str(new_bit)

        # Obtain and store the values of all individuals
        x_values = round(x_value(a, i_value(new_individual), delta_x), 4)
        fx_values = fx_value(x_values)
        i_values = i_value(new_individual)

        # Add the individual to the population
        data['Individuo'].append(new_individual)
        data['i'].append(i_values)
        data['x'].append(x_values)
        data['f(x)'].append(fx_values)

        # Add to the generation list
        generations.append((fx_values, x_values))

    return generations


def pruning(evaluate, pob_max):
    fitness = data['f(x)']

    if evaluate:
        value = min(fitness)
    else:
        value = max(fitness)

    index = fitness.index(value)

    values_i = {column: data[column][index] for column in data}

    while len(fitness) > pob_max - 1:
        randint = random.randint(0, len(fitness) - 1)

        for column in data:
            del data[column][randint]

    exists = any(all(data[column][i] == values_i[column] for column in data) for i in range(len(data['f(x)'])))

    if exists:
        for i in range(len(data['f(x)']) - 1, -1, -1):
            if all(data[column][i] == values_i[column] for column in data):
                for column in data:
                    del data[column][i]

    rdm_position = random.randint(0, len(data['f(x)']) - 1)

    for column in data:
        data[column].insert(rdm_position, values_i[column])


def maximus_and_minimus(evaluate):
    fitness = data['f(x)']

    if evaluate:
        best = min(fitness)
        worst = max(fitness)
    else:
        best = max(fitness)
        worst = min(fitness)

    average_evaluated = sum(fitness) / len(fitness)

    return best, worst, average_evaluated
