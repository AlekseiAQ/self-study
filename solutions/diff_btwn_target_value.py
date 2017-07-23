from collections import defaultdict


def some_function(target, values):
    if not values:
        return None
    results = {elem: abs(target - elem) for elem in values}
    new_results = defaultdict(list)
    for k, v in results.items():
        new_results[v].append(k)
    closest = min(new_results)
    return min(new_results.get(closest))
