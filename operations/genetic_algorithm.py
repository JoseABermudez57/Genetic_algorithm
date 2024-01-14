import math
import random

data = {
    'Individuo': [],
    'i': [],
    'x': [],
    'f(x)': []
}


def gen_base_values(a, b, delta_x_tch):
    graphic_range = b - a
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
    x_values = [round(a + i * delta_x, 4) for i in random_nums]
    fx_values = [round((pow(i, 3) - 2 * (pow(i, 2)) * math.cos(math.radians(i)) + 3), 4) for i in x_values]

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

    gen_mutation_children(find_gen_mutation_rate, prob_gen_mutation, delta_x, a)


def x_value(a, i, delta_x):
    return a + i * delta_x


def i_value(individual):
    return int(individual, 2)


def fx_value(i):
    return round((pow(i, 3) - 2 * (pow(i, 2)) * math.cos(math.radians(i)) + 3), 4)


def gen_mutation_children(fnd_mutation_rate, prob_gen_mutation, delta_x, a):

    for binary_string in fnd_mutation_rate:
        new_individual = ''
        for bit in binary_string:
            random_number = round(random.random(), 2)

            if random_number <= prob_gen_mutation:
                new_bit = 1 - int(bit)
            else:
                new_bit = int(bit)

            new_individual += str(new_bit)

        data['Individuo'].append(new_individual)
        data['i'].append(i_value(new_individual))
        data['x'].append(round(x_value(a, i_value(new_individual), delta_x), 4))
        data['f(x)'].append(fx_value(i_value(new_individual)))


def pruning(evaluate, pob_max):
    fitness = data['f(x)']
    deleted = []

    if evaluate == 1:
        value = min(fitness)
    else:
        value = max(fitness)

    new_list_wht_the_best = [element for element in fitness if element != value]

    randint = random.randint(0, len(new_list_wht_the_best) - 1)

    eliminate = random.sample(range(len(new_list_wht_the_best)), randint)

    while len(eliminate) <= pob_max:
        deleted = [x for i, x in enumerate(new_list_wht_the_best) if i not in eliminate]

    return deleted


def maximus_and_minimus(evaluate):
    fitness = data['f(x)']

    if evaluate == 1:
        best = min(fitness)
        worst = max(fitness)
    else:
        best = max(fitness)
        worst = min(fitness)

    avergare_evaluated = sum(fitness) / len(fitness)

    return best, worst, avergare_evaluated
