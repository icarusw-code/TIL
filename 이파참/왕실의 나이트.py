input_data = input()
row = int(input_data[1]) #a2 일경우 1번 인덱스가 숫자가 된다 (가로)
column = int(ord(input_data[0]))-int(ord('a')) + 1 # a를 빼줌으로 초기화하고 +1 로 출발 (세로)

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0 
for step in steps:
    next_row = row +step[0] 
    next_column = column +step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result += 1

print(result)