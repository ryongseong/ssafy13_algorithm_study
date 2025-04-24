def find_set(n):
    if boss[n] == n: return n
    boss[n] = find_set(boss[n])
    return boss[n]

def union_set(t1, t2):
    a = find_set(t1)
    b = find_set(t2)
    if a == b: return
    if a < b:
        boss[b] = a
    else:
        boss[a] = b

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    boss = [i for i in range(N+1)]
    edges = []
    for _ in range(M):
        s, e, c = map(int, input().split())
        edges.append((c, s, e))

    edges.sort()

    sum_v = 0
    cnt = 0

    for cost, a, b in edges:
        if find_set(a) == find_set(b): continue
        union_set(a, b)
        cnt += 1
        sum_v += cost

    print(f'#{tc} {sum_v}')