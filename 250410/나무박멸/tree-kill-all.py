# # n*n칸 / 총 m년 ('성장 번식 제초'를 m세트 씩) / 제초 대각선으로 k 칸 / c년 동안 유효
# n, m, k, c = map(int, input().split())

# # 1~ 나무 그루 수
# # 0 빈 칸
# # -1 벽
# # -2 부터 안쓰임.
# # -2 -> 에 -m으로 제초 시간을 체크
# # 즉, -7 이면 5년 남은 것.
# # 다만, 제초 시간 처리 할 때 -2 는 0으로 다시 치환해주는 작업 필요
# # -> 이러면 무조건 0이상인건 나무 라고 처리 가능
# arr = [list(map(int, input().split())) for _ in range(n)]


# # 1) 성장
# # 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 성장 - 상하좌우 서로
# # (모든 나무 동시에)
# def grow():
#     global arr
#     # 이동하면서 전의 결과에 영향을 안받으려면 새로 만드는 수 밖에 없나
#     for i in range(n):
#         for j in range(n):
#             # 1) 4방향 다 뿌리고
#             # 나무라면
#             if arr[i][j] > 0:
#                 for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                     nx, ny = i + dx, j + dy
#                     if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
#                         arr[i][j] += 1
#     return arr


# # 2) 번식
# # 벽 => X
# # 나무 => 성장
# # 제초제 => X
# # 나머지 => 번식
# # (각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼)
# # 즉, 위 왼쪽 2개로 번식 된다. -> 본인 나무 7 -> 7 // 2 -> 3만큼 위 왼쪽으로 번식
# def breed(arr):
#     # 이동하면서 전의 결과에 영향을 안받으려면 새로 만드는 수 밖에 없나
#     new_arr = [row[:] for row in arr]
#     for i in range(n):
#         for j in range(n):
#             # 나무라면
#             if arr[i][j] > 0:
#                 # print(f'[번식] {i}, {j} 인덱스의 나무 : {arr[i][j]}')
#                 # 1) 벽(-1), 다른 나무(1 이상), 제초제(-2), 범위 체크
#                 # => 그냥 0인 곳에 번식하면 되지 않나? [아직은 맞는거 같음 나중에 case 재검토]
#                 # 번식 가능한 곳의 [좌표]를 먼저 담아둔다.
#                 temp = []
#                 for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                     nx, ny = i + dx, j + dy
#                     if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
#                         temp.append([nx, ny])
#                 if temp:
#                     # print(f'[번식] 번식 가능 나무 : {arr[i][j]}, 번식 가능 칸 개수 : {len(temp)}')
#                     # print(f'[번식] 번식 가능 한 좌표 {temp}, 각 칸 번식 나무 수 : {arr[i][j] // len(temp)}')
#                     for t in temp:
#                         x, y = t
#                         new_arr[x][y] += (arr[i][j] // len(temp))
#     return new_arr


# # 3) 제초제
# # - 제초제를 뿌렸을 때 가장 많이 박멸되는 칸에 제초제를 뿌린다.
# # 1. 나무가 없는 칸에 뿌리는 경우
# # -- 박멸되는 나무 X
# # 2. 나무가 있는 칸에
# # 2-1. k의 범위 만큼 대각선으로 전파. 다 박멸됨
# # 2-2. 벽이 있는 경우 전파 X
# # c년 만큼 그 자리에 유효
# # 유효 끝나기 전에 다시 그 자리에 뿌려진다면 c년을 초기화 시켜야 한다.
# def destroy():
#     global arr, c, k
#     # 각 칸에 제초제 뿌릴 경우 얼만큼의 나무를 제초할 수 있나 -> temp에 저장
#     temp = [[-1 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             # 1. 나무가 없는 칸에 뿌리는 경우 -> 박멸 X
#             # 2. 나무가 있는 곳에 뿌릴 경우
#             # for 모든 곳에서 체크
#             # for 4 가지 대각선 방향으로,
#             # 범위 내 까지 옮겨 가며 체크
#             # 나무 라면, 합산 -> temp 좌표에 합산을 저장 -> 가장 큰 값의 시작 좌표를 찾는다.
#             if arr[i][j] >= 0:
#                 sum_tree = arr[i][j]
#                 for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
#                     nx, ny = i, j
#                     k_count = 0
#                     condition = True
#                     while condition:
#                         nx, ny = nx + dx, ny + dy
#                         k_count += 1
#                         # [중요 조건] : k칸 까지. k 넘어가면. 전파 끝
#                         # [중요 조건] : 벽이나 빈칸을 만나면 거기서 끝. 전파 끝
#                         if (0 <= nx < n and 0 <= ny < n) and k_count <= k and arr[nx][ny] != -1:
#                             # 나무 일 때만 합산 - 제초제인 경우 제거
#                             if arr[nx][ny] > 0:
#                                 sum_tree += arr[nx][ny]
#                             elif arr[nx][ny] == 0:
#                                 condition = False
#                         else:
#                             condition = False
#                 temp[i][j] = sum_tree
#             elif arr[i][j] == 0:
#                 temp[i][j] = 0

#                 # print(f'[번식] {i}, {j}에 제초제를 뿌릴 경우: {sum_tree}')
#     # print(f'[제초] 각 칸에 제초제를 놓는 경우 박멸되는 나무의 수 : {temp}')

#     max_val = float('-inf')
#     max_pos = (-1, -1)
#     # max 값 찾기
#     # 만약 가장 많은 나무를 박멸시킬 곳이 여러 군데라면?
#     # 1. 행이 작은 순 / -> 2. 열이 작은 순 = 자동으로 됨. 처음 잡히는 max. 같아도 더 크지 않으면 안바뀜
#     for i in range(n):
#         for j in range(n):
#             if temp[i][j] > max_val:
#                 max_val = temp[i][j]
#                 max_pos = (i, j)
#     # print(f'[제초] max 후보 : {max_temp}, 최종 max 좌표 : {max_temp[0][0]}, 최종 max : {max_temp[0][1]}')

#     # 제초제 실제로 놓기
#     # 2가지 처리, 실제 map -> -(2+)로 변경
#     # 제초 map에 시간 쓰기
#     i, j = max_pos

#     arr[i][j] = -(2 + c)

#     for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
#         nx, ny = i, j
#         k_count = 0
#         condition = True
#         while condition:
#             nx, ny = nx + dx, ny + dy
#             k_count += 1
#             # [중요 조건] : k칸 까지. k 넘어가면. 전파 끝
#             # [중요 조건] : 벽이나 빈칸을 만나면 거기서 끝. 전파 끝
#             if (0 <= nx < n and 0 <= ny < n) and k_count <= k and arr[nx][ny] != -1:
#                 # 나무 일 때만 합산 - 제초제인 경우 제거
#                 # 그리고 / 제초제 만나면 초기화
#                 # [주의] 남아 있는 년도가 더 작을 때만 초기화.
#                 # 즉, -로 표기되므로 더 클 때 초기화
#                 if arr[nx][ny] > 0 or (-2 > arr[nx][ny] > -(2 + c)):
#                     arr[nx][ny] = -(2 + c)
#                 elif arr[nx][ny] == 0:
#                     arr[nx][ny] = -(2 + c)
#                     condition = False
#             else:
#                 condition = False
#             # print(arr)

#     return max_val


# def time_go():
#     global arr
#     # 제초 남은 연도 체크
#     for i in range(n):
#         for j in range(n):
#             # 1. "-2 미만인 곳 모두 +1 처리"
#             if arr[i][j] < -2:
#                 arr[i][j] += 1
#             # 2. -2된 곳 (means 0년 됨) -> 0으로 치환
#             if arr[i][j] == -2:
#                 arr[i][j] = 0
#     return arr


# # 성장, 번식, 제초 작업이 한 세트로 1년에 걸쳐 진행된다
# # m년 동안 총 박멸한 나무의 그루 수를 작성한다.

# # 마지막에 세트를 m년 반복
# answer = 0
# for i in range(m):
#     # print(i, "년 처리 ----------------")
#     # c년만큼 남아있고, c+1년이 될 때 사라진다.
#     if i >= 1:
#         time_go()
#     #     print("= 1년 처리 :")
#     #     for column in arr:
#     #         print(column)
#     # print("0. 초기 상태")
#     # for column in arr:
#     #     print(column)
#     grow()
#     # print("1. 성장 후 상태:")
#     # for column in arr:
#     #     print(column)
#     arr = breed(arr)
#     # print("2. 번식 후 상태 :")
#     # for column in arr:
#     #     print(column)
#     max_val = destroy()
#     answer += max_val
#     # print("3. 제초 후 상태 :")
#     # for column in arr:
#     #     print(column)
#     # print(f'현재까지의 max 제초 : {answer}')

# print(answer)

n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pesticide = [[0]*n for _ in range(n)]

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def grow():
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                cnt = 0
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] > 0:
                        cnt += 1
                temp[x][y] = cnt
    for i in range(n):
        for j in range(n):
            arr[i][j] += temp[i][j]

def breed():
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                cand = []
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0 and pesticide[nx][ny]==0:
                        cand.append((nx, ny))
                if cand:
                    spread = arr[x][y] // len(cand)
                    for nx, ny in cand:
                        temp[nx][ny] += spread
    for i in range(n):
        for j in range(n):
            arr[i][j] += temp[i][j]

def get_best_spot():
    max_kill, best_pos = 0, (0, 0)
    for x in range(n):
        for y in range(n):
            if arr[x][y] <= 0:
                continue
            kill = arr[x][y]
            for dx, dy in diag:
                for step in range(1, k+1):
                    nx, ny = x + dx*step, y + dy*step
                    if not (0<=nx<n and 0<=ny<n): break
                    if arr[nx][ny] == -1: break
                    if arr[nx][ny] == 0:
                        kill += 0
                        break
                    kill += arr[nx][ny]
            if kill > max_kill:
                max_kill = kill
                best_pos = (x, y)
    return best_pos, max_kill

def spray(x, y):
    if arr[x][y] > 0:
        pesticide[x][y] = c+1
        arr[x][y] = 0
    for dx, dy in diag:
        for step in range(1, k+1):
            nx, ny = x + dx*step, y + dy*step
            if not (0<=nx<n and 0<=ny<n): break
            if arr[nx][ny] == -1: break
            pesticide[nx][ny] = c+1
            if arr[nx][ny] == 0:
                break
            arr[nx][ny] = 0

def decrease_pesticide():
    for i in range(n):
        for j in range(n):
            if pesticide[i][j] > 0:
                pesticide[i][j] -= 1

result = 0
for year in range(m):
    grow()
    breed()
    pos, killed = get_best_spot()
    spray(*pos)
    decrease_pesticide()
    result += killed

print(result)
