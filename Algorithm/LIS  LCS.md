# LIS / LCS 

------

### LIS (Longest Increasing Subsequence) : (순서를 유지한채 )가장 긴 증가하는 부분 수열

**해결 방법**

1. **Dynamic Programming(동적 계획법)**
2. **Binary Search(이분 탐색)**

**Dynamic Programming**

```python
# DP 
# n = 수열 A의 크기 
# arr = 수열 A를 이루고 있는 A(i)를 담은 배열
# dp = arr[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이

# 만들어 놓은 증가수열에 ai(마지막으로 뽑은수)를 붙일 수 있으려면
# 1. 만들어 놓은 증가 수열이 ai(마지막으로 뽑은 수) 앞에 있어야 하고(j<i)
# 2. 마지막 수가 ai(마지막으로 뽑은 수) 보다 작아야 한다. (aj < ai)
n = int(input())

arr = list(map(int, input().split()))

# arr[i] 를 마지막 원소로 가질 때 가장 긴 증가하는 부분수열 길이
dp = [1 for i in range(n)] # 1로 모두 초기화

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1) # 뒤에 하나 더 붙이는 것이므로 +1을 해준다.

print(max(dp))
```

예를 들어 i = 4일때를 확인해보자.

i = 4 j = 0 dp[4] =1

arr[4] > arr[0] true 이므로 dp[4] = max(dp[4], dp[0] + 1) 2이다.

i = 4 j = 1 dp[4] = 2

arr[4] > arr[1] false

i = 4 j = 2 dp[4] = 2

arr[4] > arr[2] true이므로 dp[4] = max(dp[4], dp[2] + 1) 2이다.

i = 4 j = 3 dp[4] = 2

arr[4] > arr[3] false

|   arr   |  10  |  20  |  10  |  30  |  20  |  50  |
| :-----: | :--: | :--: | :--: | :--: | :--: | :--: |
| max_len |  1   |  2   |  1   |  3   |  2   |  4   |

**Binary Search 1**

- dp[i] 를 구하기 위해 dp[0] ~dp[i - 1] 의 최댓값을 알고 있다면 반복하지 않아도 된다. 
- python 의 **bisect** 를 사용

```python
from bisect import bisect_left
# 12015 BOJ
# 1. dp를 arr[0]으로 초기화한다.
# 2. 현재 위치(i)가 이전 위치의 원소들보다 크면 dp에 추가한다.
# 3. 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면, bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index값을 구한다. 그리고 dp의 index 원소를 arr[i]로 바꿔준다.
# 4. dp의 길이를 출력한다.

n = int(input())
arr = list(map(int, input().split()))

# dp 는 가장 긴 증가하는 부분 수열을 저장할 배열
dp = [arr[0]] # dp 를 arr[0]으로 초기화

for i in range(n):
  	# 현재 위치(i) 가 이전 위치의 원소들보다 크면 dp 에 추가한다.
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    # 자신보다 큰 수 중 최소값과 대치(이진탐색 이용)
 	else:
        dp[bisect_left(dp, arr[i])] = arr[i]
        
print(len(dp))
```

**Binary Search 최종**

DP를 이용했을때와 Binary Search 를 이용했을때 단순히 최대 길이는 구할 수 있지만 그 안에 있는 리스트를 구할 수는 없는 문제점이 있다. 이를 해결하기 위한 코드이다.

![](C:\Users\최성진\Desktop\프로그래밍\MarkDown\Algorithm\LIS 리스트 구하는 모델.jpg)

```python
#14002 BOJ
n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
# dp의 최대값을 order로 설정한다.
order = max(dp)
tmp = []
# order가 끝에 위치하므로 1씩 줄여가면 역으로 반복문을 탐색한다.
for i in range(n-1, -1, -1):
    if dp[i] == order:
        tmp.append(arr[i])
        order -= 1
# tmp에 저장된 리스트는 역순이므로 reverse 하여 출력하도록 한다.
print(*tmp[::-1])
```

