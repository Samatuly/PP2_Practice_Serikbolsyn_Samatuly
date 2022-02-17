import math

y = int(input())
def filter_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
print(list(filter(filter_prime, range(y))))