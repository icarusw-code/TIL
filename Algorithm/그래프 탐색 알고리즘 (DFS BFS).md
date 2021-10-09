# 그래프 탐색 알고리즘: DFS/BFS

------

- **스택 자료구조**

  먼저 들어온 데이터가 나중에 나가는 형식(선입 후출)

  나무가 쌓여 있는 형태

  ```python
  stack = []
  # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  
  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()
  
  print(stack[::-1]) #[1, 3, 2, 5] 최상단 원소부터 출력
  print(stack) # [5, 2, 3, 1] 최하단 원소부터 출력
  ```

-  **큐 자료구조**

  먼저 들어 온 데이터가 먼저 나가는 형식(선입 선출)

  입구와 출구가 모두 뚫려 있는 터널과 같은 형태 

  ```python
  #리스트 자료형을 사용해도 되지만 시간 복잡도가 높아 비효율적으로 동작 할 수도 있음
  from collections import deque 
  
  queue = deque()
  # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  
  queue.append(5)
  queue.append(5)
  queue.append(5)
  queue.append(5)
  queue.popleft() #제거할때는 popleft()를 쓰는것이 관행
  queue.append(5)
  queue.append(5)
  queue.popleft()
  
  print(queue) #먼저 들어온 순서대로 출력 deque([3, 7, 1, 4])
  queue.reverse()
  print(queue) #나중에 들어온 원소부터 출력 deque([4, 1, 7, 3]
  ```

- **재귀 함수 (Recursive Function)**

  자기 자신을 다시 호출하는 함수

  ```python
  def recursive_function():
  	print('재귀 함수를 호출 합니다')
  	recursive_function()
  
  recursive_functuon()
  ```

  첫줄에 반드시 재귀함수 종료 조건을 명시해야 한다

  ```python
  # n!값 구하기
  def factorial_recursive(n):
  	if n<=1:
  		return 1
  	return n*factorial_recursive(n-1)
  ```

- **DFS (Depth-First-Search)**

  DFS는 깊이 우선 탐색으로 불리며, 깊은 부분을 우선으로 탐색하는 알고리즘

  DFS는 **스택 자료구조(혹은 재귀함수**)를 이용한다.

  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.

  2. 스택 **최상단 노드**에 방문하지 않은 인접 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리 

     방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

  ```python
#낮은 숫자부터
  
  #DFS 메서드 정의
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
          
  
  ```
  
  ```python
1 2 7 6 8 3 4 5
  ```
  
  

- **BFS(Breadth-First-Search)****

  BFS는 너비 우선 탐색으로 불리며, 가까운 노드부터 우선으로 탐색하는 알고리즘

  BFS는 **큐 자료구조**를 이용한다.

  1. 탐색 시작 노드를 큐에 삽입하고 방문처리 한다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
  3. 더 이상 2번의 과정을 수행할 수 없을 떄까지 반복한다.

- **기본 개념**

  ```python
  from collections import deque
  
  #BFS 메서드 정의
  def bfs(graph, start, visited):
      #큐(Queue)구현을 위해 deque 라이브러리 사용
     	queue = deque([start])
      #현재 노드를 방문 처리
      visited[start] =True
      #큐가 빌 때까지 반복
      while queue:
          #큐에서 하나의 원소를 뽑아서 출력
          v = queue.popleft()
          print(v, end=' ')
          #아직 방문하지 않은 인접한 원소들을 큐에 삽입
          for i in graph[v]:
              if not visited[i]:
                  queue.append(i)
                  visited[i] = True
  
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
  
  bfs(graph, 1, visited)
  ```

  ```python
  1 2 3 8 7 4 5 6
  ```

- **2차원 배열 이용**

  ```python
  ######미로 탈출 아이디어######
  ###BOJ 2178 참조#######
  from collections import deque
  
  # n개의 줄에 m개의 정수로 미로의 정보 입력받음
  n, m = map(int, input().split())
  # 2차원 리스트의 맵 정보 입력 받기
  graph = []
  for i in range(n):
      graph.append(list(map(int, input())))
  
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  def bfs(x, y):
      # 큐(Queue) 구현을 위해 deque 라이브러리 사용
      queue = deque()
  	queue.append((x,y))
      # 큐가 빌 때까지 반복
      while queue:
          # 1. 원소를 먼저 꺼내준다.
          x, y = queue.popleft()
  		# 2. 상하좌우 위치를 확인한다.
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              # 미로의 공간을 벗어나는 경우는 무시한다.
              if nx < 0 or nx >= n or ny < 0 or ny >= m:
                  continue
              # 벽인 경우 무시(1인 경우에 이동할 수 있다.)
              if graph[nx][ny] == 0:
                  continue
              # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
              if graph[nx][ny] == 1:
                  # 직전노드의 최단거리 + 1
                  graph[nx][ny] = graph[x][y] + 1
                  queue.append((nx,ny))
      return graph[n-1][m-1]
  
  # BFS 수행한 결과 출력
  print(bfs(0, 0))
  ```
  
- 3차원 배열 이용👍

  ```python
  #BOJ 14442 벽 부수고 이동하기2 참고
  '''
  N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
  
  만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동하여도 된다.
  
  한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
  
  맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
  '''
  from collections import deque
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # N x M, 벽개수
  n, m, l = map(int, input().split())
  
  board = [list(map(int, list(input()))) for _ in range(n)]
  
  # 이동 거리를 저장 (l 은 벽을 부순 횟수를 의미한다.)
  dist = [[[0] * (l + 1) for j in range(m)] for i in range(n)]
  
  queue = deque()
  queue.append((0,0,0))
  dist[0][0][0] = 1
  while queue:
      x, y, z = queue.popleft()
      for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          # board 범위 안에 들어옴
          if 0<= nx < n and 0 <= ny < m:
              # 벽을 부수지 않는 경우(이동할 수 있는 상태(0) 
              if board[nx][ny] == 0 and dist[nx][ny][z] == 0:
                  dist[nx][ny][z] = dist[x][y][z] + 1
                  queue.append((nx, ny, z))
              # 벽을 만났고, 벽을 부수는 경우
              if z + 1 <= l and board[nx][ny] == 1 and dist[nx][ny][z + 1] == 0:
                  dist[nx][ny][z + 1] = dist[x][y][z] + 1
                  queue.append((nx, ny, z + 1))
  
  ans = -1 
  for i in range(l + 1):
      if dist[n-1][m-1][i] == 0:
          continue
  	if ans == -1:
          ans = dist[n -1][m - 1][i]
      elif ans > dist[n - 1][m - 1][i]:
          ans = dist[n - 1][m - 1][i]
  print(ans)
  
  ```

  ```python
  ###부가설명###
  ###참조한 블로그###
  from sys import stdin
  from collections import deque
  input = stdin.readline
  
  n, m, k = map(int, input().split())
  a = [list(input()) for _ in range(n)]
  dist = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
  dx = (-1, 0, 1, 0)
  dy = (0, 1, 0, -1)
  
  def bfs():
      q = deque()
      q.append((0, 0, 0))
      dist[0][0][0] = 1
      while q:
          x, y, w = q.popleft()
          if x == n-1 and y == m-1:
              return dist[n-1][m-1][w]
          for i in range(4):
              nx, ny, nw = x+dx[i], y+dy[i], w+1
              if nx < 0 or nx >= n or ny < 0 or ny >= m:
                  continue
              if dist[nx][ny][w]:
                  continue
              if a[nx][ny] == '0':
                  dist[nx][ny][w] = dist[x][y][w] + 1
                  q.append((nx, ny, w))
              if a[nx][ny] == '1' and nw <= k:
                  dist[nx][ny][nw] = dist[x][y][w] + 1
                  q.append((nx, ny, nw))
      return -1
  
  print(bfs())
  
  
  출처: https://rebas.kr/659 [PROJECT REBAS]
  ```

  


|               |      DFS       |       BFS        |
| :-----------: | :------------: | :--------------: |
| **동작 원리** |      스택      |        큐        |
| **구현 방법** | 재귀 함수 이용 | 큐 자료구조 이용 |

## **0-1 BFS 에 관하여**

[참조하면 좋은 블로그]: https://medium.com/@jypthemiracle/%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC-%EB%AC%B8%EC%A0%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B6%81%EA%B8%88%EC%A6%9D-%EC%A0%95%EB%A6%AC-5b1b813ba1b3

### **개요**

최단 경로 문제

|       그래프 종류        |                       최단 경로                       |
| :----------------------: | :---------------------------------------------------: |
|   가중치가 없는 그래프   |         두 정점을 잇는 가장 적은 간선의 개수          |
| 가중치가 존재하는 그래프 | 두 정점을 잇는 간선들의 가중치의 합 중 최소 가중치 합 |

### Point1. 최단 경로 탐색할 때 DFS를 사용하지 않는 이유

- 방향성이 없는 udirected graph 가정해보자

- 안 될 이유는 없지만, 비효율적이다.

- 최단경로를 검색할 때 recursive 하게 DFS를 구현하면 내가 원하는 간선간의 거리를 구할 수 있지만, 트리 형태라는 확증이 있어야 한다.

- 만약 그래프의 경우라면 내가 최종적으로 방문한 경로가 최단 경로인지 확신 할 수 없다

  반대로, 트리의 경우라면 정점 간의 경로가 단 하나만 존재하기 때문에, 내가 방문한 경로는 무조건 최단경로이다.

### Point2. 가중치가 있는 그래프에서 DFS와 BFS를 사용할 수 있는 이유

- 가중치가 없는 그래프인 경우 BFS를 사용할 수 있다.
- 이와함께 간선에 가중치가 존재한다면 BFS를 사용할 수 없다는 것도 익히 알려져 있다.
- 단순히 depth로만 최단 거리가 정해지는 것이 아니기 때문이다. depth(층위)에 있는 노드끼리 이동하는 것은 고려하지 않는다.
- 예를 들어, A가 B와 C와 연결되어 있고 B와 C가 서로 연결되어 있다고 하자. 그렇다면 노드 A는 depth가 1이고, B, C는 depth가 2가 된다. A-B가 가중치 3, A-C가 가중치 1, B-C가 가중치 1라고 가정하자. 노드 B로 가는 최단 경로는 무엇일까? depth를 기준으로 하면 노드 A -> 노드 C가 된다. 하지만 이는 가중치를 고려하지 않은 경우이다. weight을 고려하면 노드 A -> 노드 C -> 노드 B가 가중치를 가장 적게 고려하는 경우가 되지만, depth를 기준으로 탐색하는 BFS에서는 해당 경로가 고려되지 않는다.

### Point3. 가중치가 있는 그래프에서 다익스트라 알고리즘을 쓰는 이유

- 가중치가 있는 그래프에서 BFS를 사용할 수 없는 이유는, BFS가 Greedy한 알고리즘이 아니기 때문이다. 이와 달리, 다익스트라 알고리즘은 Greedy하다. 그리디한 이유는 최소 거리에 최소 거리를 붙이면 최소 거리가 될 것이다라는 논리가 함축되어 있기 때문이다.

### Point4. 가중치가  0과1만 존재하는 그래프에서 BFS를 쓰는 이유

- 어느 임의의 그래프에서 간선 (u, v)를 지난다고 가정해보자. 가중치가 0과 1만 존재하므로, 우리는 간선 (u, v)를 지날 때 노드 u와 v에 대해 다음의 사항을 고려할 수 있다.
- v는 u와 같은 레벨이다. 즉, 가중치가 0이라는 것은 v는 u와 같은 레벨이다.
- v는 u의 1레벨 아래이다. 즉, 가중치가 1이라는 것은 v는 u의 1레벨 아래이다.

- 우리가 노드 u에 있을 때, queue에는 level이 *L[u]* 또는 *L[u] + 1* 이라는 두 가지의 사항만 포함되어 있다는 사실을 알 수 있다. 

- 노드 v의 최단거리가 단축되었다면 deque의 앞 부분에 넣어준다.

- 노드 u와 같은 레벨이라면 deque의 뒷 부분에 넣어준다.

  |       가중치        |     행동     |
  | :-----------------: | :----------: |
  | 0(같은 레벨인 경우) | Front에 삽입 |
  | 1(다른 레벨인 경우) | Back에 삽입  |

  

