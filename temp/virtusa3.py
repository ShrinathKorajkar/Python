import math
import heapq


def dijkstra(adj_list, start):
    n = len(adj_list)
    dist = [math.inf] * n
    dist[start] = 0
    visited = [False] * n
    heap = [(0, start)]

    while heap:
        (d, u) = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for (v, w) in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


n = int(input())
adj_list = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, t = map(int, input().split())
    adj_list[a - 1].append((b - 1, t))
    adj_list[b - 1].append((a - 1, t))

travel_times = [[math.inf] * n for _ in range(n)]

for u in range(n):
    for (v, w) in adj_list[u]:
        estimated_time = math.ceil(w / 60)
        travel_times[u][v] = estimated_time
        travel_times[v][u] = estimated_time

actual_travel_times = []
for u in range(n):
    actual_travel_times.append(dijkstra(adj_list, u))

largest_error = 0
for u in range(n):
    for v in range(n):
        if u == v:
            continue
        error = abs(actual_travel_times[u][v] - 60 * travel_times[u][v])
        largest_error = max(largest_error, error)

print(largest_error)