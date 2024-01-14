import math


def gen_base_values(a, b, bits_length, delta_x_tch):
    ranges = b - a
    jumps_tch = ranges / delta_x_tch
    points_tch = jumps_tch + 1
    qt_bits_tch = math.ceil(math.log(points_tch, 2))
    if 2 ** (qt_bits_tch - 1) < points_tch <= 2 ** qt_bits_tch:
        print("correcto", qt_bits_tch)
    else:
        print("incorrecto", qt_bits_tch)

    print("_______________________")

    delta_x = ranges / (pow(2, bits_length) - 1)
    jumps = ranges / delta_x
    points = jumps + 1
    qt_bits = math.ceil(math.log(points, 2))
    if 2 ** (qt_bits - 1) < points <= 2 ** qt_bits:
        print("correcto", qt_bits)
    else:
        print("incorrecto", qt_bits)
