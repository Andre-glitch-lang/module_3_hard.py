def calculate_structure_sum(args):
    total = 0
    if isinstance(args, (int, float)):
        total += args
    elif isinstance(args, str):
        total += len(args)
    elif isinstance(args, (list, tuple, set)):
        for element in args:
            total += calculate_structure_sum(element)
    elif isinstance(args, dict):
        for key, value in args.items():
            total += calculate_structure_sum(value)
            total += calculate_structure_sum(key)

    return total


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)