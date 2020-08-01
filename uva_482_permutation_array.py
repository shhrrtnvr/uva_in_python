tc = int(input())
for t in range(tc):
    blank, p_array, data = input(), map(int, input().strip().split()), input().strip().split()
    if t: print()
    permutation = [0]*len(data)
    for i, j in enumerate(p_array): permutation[j-1] = data[i] 
    for val in permutation: print(val)

