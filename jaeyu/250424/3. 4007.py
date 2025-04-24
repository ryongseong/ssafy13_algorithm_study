import heapq

def dijkstra(start, graph):
    times = [float('inf')] * (N+1)
    times[start] = 0
    q = [(0, start)]

    while q:
        time, node = heapq.heappop(q)
        if times[node] < time: continue

        for next, next_time in graph[node]:
            if times[next] > times[node] + next_time:
                times[next] = times[node] + next_time
                heapq.heappush(q, (times[next], next))

    return times

def calc():
    global max_v

    go = dijkstra(X, reverse) # start가 X이니까 강의실에서 X로 가는 거는 reverse 이용
    back = dijkstra(X, graph) # X에서 강의실로 가는 거 

    for i in range(1, N+1):
        total = go[i] + back[i]
        max_v = max(max_v, total)

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    reverse = [[] for _ in range(N+1)]
    max_v = float('-inf')

    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        reverse[e].append((s, t))

    calc()

    print(f'#{tc} {max_v}')