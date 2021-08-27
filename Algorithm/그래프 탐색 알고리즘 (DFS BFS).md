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

  ![](C:\Users\최성진\Desktop\프로그래밍\이코테\DFS.JPG)

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

  

- **BFS(Breadth-First-Search)****

  BFS는 너비 우선 탐색으로 불리며, 가까운 노드부터 우선으로 탐색하는 알고리즘

  BFS는 **큐 자료구조**를 이용한다.

  1. 탐색 시작 노드를 큐에 삽입하고 방문처리 한다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
  3.  더 이상 2번의 과정을 수행할 수 없을 떄까지 반복한다.

  ![](C:\Users\최성진\Desktop\프로그래밍\이코테\DFS.JPG)

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

  

