# 배낭 문제(Knapsack Algorithm)

------

### Greedy  Approach

- **분할 가능한 문제일 경우(Fractional Knapsack Problem)**

- 가장 값어치가 높은 아이템을 먼저 채움

- 1kg당 가격을 기준으로 내림차순 정렬

- 배낭의 무게를 초과하지 않을때 까지 비싼 순으로 채우기

  ```python
  def knapsack(W, w, p): #전체 무게, 각 아이템 무게, 가치
      n = len(w) - 1 # 1번부터
      K = [0] * (n + 1) # 담을 공간
      weight = 0
      for i in range(1, n + 1):
          weight += w[i]
          if (weight > W):
              K[i] -= (weight - W)
              break
    	return K
  ```

## **만약 아이템의 분할이 불가능한 경우(0-1 배낭문제)**

- 최적화 문제이며, 탐욕 알고리즘은 최적해를 보장하지 않는다.

### 동적 계획법

**1)2차원 해결**

```python
# P[i][w]: 총 무게가 w를 초과할 수 없다는 제약 조건하에서 처음 i개 아이템에서만 선택 할 때 얻는 최적의 이익
# P[n][w]: n개의 아이템으로 얻을 수 있는 최대 이익
# P[i-1][w]: i-1개의 아이템을 가지고 구한 전 단계의 최적값
# Pi + P[i-1][w-wi]: i번쨰 아이템을 위해 i번째 아이템만큼의 무게를 비웠을때 최적값에 i번째 아이템을 더한 값
# 
```

$$
P[i][w] = P[i-1][w](w_i > w)\quad Max(P[i-1][w],\quad p_i + p[i-1][w-w_i])(w_i \leq w)
$$

[https://gsmesie692.tistory.com/113]: 

```python
def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    P = [[0 for x in range(W+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(W+1):  # 각 칸을 돌면서
            if i==0 or w==0:  # 0번째 행/열은 0으로 세팅
                P[i][w] = 0
            elif wt[i-1] <= w:  # 점화식을 그대로 프로그램으로
                P[i][w] = max(val[i-1]+P[i-1][w-wt[i-1]], P[i-1][w])  # max 함수 사용하여 큰 것 선택
            else:
                P[i][w] = P[i-1][w]
    return P[n][W]

wt = []
val = []
N, P = map(int, sys.stdin.readline().strip().split())
for i in range(N):
    w, v = map(int, sys.stdin.readline().strip().split())
    wt.append(w)
    val.append(v)
print(knapsack(P, wt, val, N))
```

**2) 1차원 해결(시간이 짧게 걸림)**

- limit 뒤에서 부터 시작

```python
# n:보석의 종류/ limit:무게 제한
# 보석 선택이 여러번 가능
n, limit = map(int, input().split())

# dy리스트의 인덱스 = 인덱스 만큼의 무게에서 갖는 최대한의 가치
# limit + 1을 해줘야 인덱스 번호가 limit 까지 생긴다
dy = [0] * (limit+1)

for i in range(n):
    weight, value = map(int, input().split())
    # 선택한 물건의 가치를 포함하는 것을 적용한다고 가정하기 때문에 for문의 시작이 weight임
    # => 안그러면 음수 index
    for j in range(limit, weight-1, -1):
        # weight를 포함했다고 가정하고 value를 추가한 상태에서 순환
        # dy[j]: 기존에 저장된 값
        # j - weight : weight에 해당하는 값을 담아야하므로 전체 무게에서 weight 만큼의 여유공간 확보
        # + value : 확보한 여유공간까지 값 + weight의 값 
        dy[j] = max(dy[j], dy[j-weight] + value)

print(dy[limit])
```

