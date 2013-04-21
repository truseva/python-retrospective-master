def groupby(func, seq):
    dictionary = {}
    for element in seq:
        dictionary.setdefault(func(element), []).append(element)
    return dictionary


def compose(func1, func2):
    def result(x):
        return func1(func2(x))
    return result


def iterate(func):
    result = lambda x: x
    yield result
    while True:
        result = compose(func, result)
        yield result


def zip_with(func, *iterables):
    for iterables in zip(*iterables):
        yield func(*iterables)


def cache(func, cache_size):
    if cache_size == 0:
        return func
    cache = [(None, None)]*cache_size

    def func_cached(*arguments):
        for cache_element in cache:
            if cache_element[0] == arguments:
                return cache_element[1]
        cache.pop(0)
        cache.append((arguments, func(*arguments)))
        return cache[cache_size-1][1]
    return func_cached