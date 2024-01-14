from fractions import Fraction
import pandas as pd
from operations import genetic_algorithm as ga


def start_simulation(data):
    a = int(data["a"])
    b = int(data["b"])
    pob_min = int(data["pob_min"])
    prob_mut_individual = float(data["prob_mut_individual"])
    prob_mut_gene = float(data["prob_mut_gene"])
    res = float(Fraction(data["res"]))
    pob_max = int(data["pob_max"])
    iterations = int(data["iterations"])
    max_or_min = data["max_or_min"]

    qt_bits, delta_x = ga.gen_base_values(a, b, res)
    ga.gen_individuals(pob_min, qt_bits, a, delta_x)

    df = pd.DataFrame(ga.data)
    df.index = df.index + 1

    print(df)

    for _ in range(iterations):
        couples = ga.generate_couples(ga.data.get('Individuo'), len(ga.data))
        children = ga.crossover_pairs(couples)
        ga.mutate_pob(children, prob_mut_individual, prob_mut_gene, delta_x, a)
        print(ga.data.get("Individuo"))

    print(pd.DataFrame(ga.data))

    print("_________________________")
