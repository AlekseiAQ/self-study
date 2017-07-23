def some_function(target, values):
    if not values:
        return None
    results = {elem: abs(target - elem) for elem in values}
    new_results = {}
    for k, v in results.items():
        new_results.setdefault(v, []).append(k)
    closest = min(new_results)
    return min(new_results.get(closest))
