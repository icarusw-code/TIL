# 소수(Prime Number)  판별

------

**기본적인 알고리즘**

```python
def is_prime_number(x):
    # 2부터 (x -1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))
```

- 2부터 X-1까지의 모든 자연수에 대하여 연산을 수행해야 한다
  - 모든 수를 하나씩 확인한다는 점에서 시간 복잡도는 O(X)

**개선된 알고리즘: 약수가 대칭으로 되어 있으므로 절반만 확인**

```python
import math #제곱근을 호출하기 위해

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))
```

## 에라토스테네스의 체 알고리즘 

- 특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할 때
  1.  2부터 N까지의 모든 자연수를 나열한다
  2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다
  3. 남은 수 중에서 i 의 배수를 모두 제거한다(i는 제거하지 않는다)
  4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다

```python
import math

n = 1000 # 2부터 1000까지 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인 것으로 초기화
array = [True for i in range(n +1)]

#에라토스테네스의 체 알고리즘 수행
#2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 #배수
        while i * j <= n:
            array[i * j] = False
            j += 1
            
# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
```

