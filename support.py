import functools


def pipe(*functions):
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)
