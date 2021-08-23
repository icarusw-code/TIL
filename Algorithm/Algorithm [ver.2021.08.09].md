# Algorithm 

## **주요 라이브러리** [ver.2021.08.09]

### **itertools**

반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

*주요 클래스: permutaions, combinations

```python
from itertools import permutaions

data=['A', 'B', 'C'] #데이터 준비

result = list(permutaions(data,3)) #모든 순열 구하기

print(result)
```

