def solve(numheads, numlegs):
    for C in range(0, numheads + 1):
        R = numheads - C
        totlegs = 4 * R + 2 * C
        if totlegs == numlegs:
            return C, R
print(solve(35, 94))