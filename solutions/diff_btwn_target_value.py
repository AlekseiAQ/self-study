def some_function(target, values):
    if not values:
        return []
    results = {elem: abs(target - elem) for elem in values}
    new_results = {}
    for k, v in results.items():
        new_results.setdefault(v, []).append(k)
    closest = min(new_results)
    results = new_results.get(closest)
    return results if isinstance(results, int) else min(results)
