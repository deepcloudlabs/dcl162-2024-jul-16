import sys
from functools import reduce

sys.set_int_max_str_digits(10_000_000)
data = range(1, 1_000_000)

result = reduce(lambda m, n: m + n, map(lambda u: u ** 3, filter(lambda x: x % 2 == 0, data)))
print(result)
result = reduce(lambda m, n: m * n, range(1, 100_000), 1)
print(result)
