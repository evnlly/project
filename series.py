#content of series.py in my_math package
def get_series(n):
    return list(range(1, n))
def get_even_series(n):
    series = get_series(n)
    even_series = [i * 2 for i in series]
    return even_series
def get_odd_series(n):
    series = get_series(n)
    odd_series = [i * 2 + 1 for i in series]
    return odd_series
def get_series(n):
    return list(range(1, n)) # we made mistake