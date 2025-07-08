import random

def random_partition(n=8, total=1.0, precision=0.01):
    steps = int(total / precision)
    cuts = sorted(random.sample(range(1, steps), n - 1))
    parts = [b - a for a, b in zip([0] + cuts, cuts + [steps])]
    return [round(p * precision, 2) for p in parts]

def generate_results(keys):
    dicts = []
    result = random_partition(n=len(keys), total=1.0, precision=0.01)
    for r in cyclic_rotations(result):
        combination_dict = {}
        for i in range(len(r)):
            combination_dict[keys[i]] = r[i]
        dicts.append(combination_dict)
    return dicts


def cyclic_rotations(lst):
    return [lst[i:] + lst[:i] for i in range(len(lst))]
