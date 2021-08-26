def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

 #각 노드가 연결된 정보를 표현(2차원 리스트)

graph = [
     [], #순서를 맞추기 위해 공백으로
     [2, 3, 8], #1에 연결된 노드
     [1, 7],
     [1, 4, 5],
     [3, 5],
     [3, 4],
     [7],
     [2, 6, 8],
     [1, 7]
 ]
    
#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]*9 #모든 노드를 방문하지 않은 처리(index[0]은 사용하기 않기 위해 하나 크게)

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
        