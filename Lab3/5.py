from itertools import permutations
word = str(input())
def func(x):
    perm = permutations(x)
    for i in list(perm):
        print(*i, sep = "")

func(word)