while True:
    try: n = int(input())
    except: break
    weight = [int(input()) for _ in range(1<<n)]
    neighbor = lambda attr,i: (attr[i^(1<<j)] for j in range(n))
    potency = [sum(neighbor(weight, corner)) for corner in range(1<<n)]
    print(max((potency[corner]+max(neighbor(potency, corner)) for corner in range(1<<n))))
