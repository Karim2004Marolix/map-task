def recursive_function(x):
    if x ==1:
        return 1
    else:
        return x * recursive_function(x-1)
num = 4
print(recursive_function(num))


def sum_n(n):
    if n == 0:
        return 0
    else:
        return n+sum_n(n-1)
print(sum_n(55))


