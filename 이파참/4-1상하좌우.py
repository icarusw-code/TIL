# 입력 받기 
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type=['L', 'R', 'U', 'D'] #ex) L->(0,-1)

#이동 계획 하나씩 확인
for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    #공간 벗어나는 예외처리
    if nx<1 or ny<1 or nx> n or ny>n:
        continue

    #이동 수행
    x, y = nx, ny

print(x, y)

