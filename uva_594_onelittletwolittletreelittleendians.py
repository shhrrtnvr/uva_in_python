while True:
    try:
        n = int(input())
    except:
        break
    bits = n & 0xffffffff
    ans = 0
    op = bits & 0x000000ff
    ans = ans | (op << 24)
    op = bits & 0x0000ff00
    ans = ans | (op << 8)
    op = bits & 0x00ff0000
    ans = ans | (op >> 8)
    op = bits & 0xff000000
    ans = ans | (op >> 24)
    
    if ans & (1 << 31):
        ans -= 0x100000000
    print(n, 'converts to', ans)
