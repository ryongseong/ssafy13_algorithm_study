def dfs(lev, now, cost):
    global min_v

    if cost >= min_v: return

    if lev == N-1:
        total = cost + board[now][0] # 관리구역에서 사무실로 돌아갈 때의 사용량 더한 값
        min_v = min(min_v, total) 
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            dfs(lev + 1, i, cost + board[now][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v = float('inf')

    visited[0] = 1

    dfs(0, 0, 0)

    print(f'#{tc} {min_v}')