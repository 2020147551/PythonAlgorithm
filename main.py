import sys

# 그리디 알고리즘 1번 큰수의 법칙
#
# a, b, c = map(int, sys.stdin.readline().rstrip().split())
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
# count = 1
# total = 0
# sorted_list = sorted(num_list)
#
# for i in range(b):
#     if count % c == 0:
#         total += sorted_list[-2]
#     else:
#         total += sorted_list[-1]
#     count += 1
#
# print(total)

# 그리디 알고리즘 2번 숫자 카드 게임
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
# num_list = list()
# for i in range(a):
#     num_list.append(min(list(map(int, sys.stdin.readline().rstrip().split()))))
#
# print(max(num_list))

# 그리디 알고리즘 3번 1이 될 때까지
#
# n, k = map(int, sys.stdin.readline().rstrip().split())
# count = 0
# while True:
#     if n % k == 0:
#         if n != 1:
#             n = int(n / k)
#             count += 1
#     else:
#         n -= 1
#         count += 1
#     if n == 1:
#         break
#
# print(count)

# 그리디 알고리즘 기출문제 1번 모험가 길드
#
# num_of_people = int(sys.stdin.readline().rstrip())
# list_of_fear = list(map(int, sys.stdin.readline().rstrip().split()))
# group = 0
# count = 0
#
# list_of_fear.sort()
#
# for i in list_of_fear:
#     count += 1
#     if i <= count:
#         group += 1
#         count = 0
#
# print(group)

# 그리디 알고리즘 기출문제 2번 곱하기 혹은 더하기
#
# num_list = list(sys.stdin.readline().rstrip())
# for i in range(len(num_list)-1):
#     if int(num_list[i]) == 0 or int(num_list[i]) == 1:
#         num_list[i+1] = int(num_list[i+1]) + int(num_list[i])
#     else:
#         num_list[i+1] = int(num_list[i+1]) * int(num_list[i])
#     i += 1
#
# print(num_list[len(num_list)-1])

# 그리디 알고리즘 기출문제 3번 문자열 뒤집기

# num_list = list(map(int, sys.stdin.readline().rstrip()))
# count_zero = 0
# count_one = 0
# i = 0
# while i < len(num_list):
#     count_cons = 0
#     while i + count_cons < len(num_list) and num_list[i] == num_list[i + count_cons]:
#         count_cons += 1
#     if num_list[i] == 1:
#         count_one += 1
#     else:
#         count_zero += 1
#     i += count_cons
#
# print(min(count_zero, count_one))

# 그리디 알고리즘 기출문제 4번 만들 수 없는 금액
#############################################################7-4-2021 거의 한시간동안 풀지 못해서 답안 보고 풂##############################################################################
# num = int(sys.stdin.readline().rstrip())
#
# coin_list = list(map(int, sys.stdin.readline().rstrip().split()))
# coin_list.sort()
# target = 1
# for coin in coin_list:
#     if target < coin:
#         break
#     else:
#         target += coin
#
# print(target)

# 그리디 알고리즘 기출문제 5번 볼링공 고르기


# 구현 알고리즘 예제 4-1번
#
# def move(input):
#     global a, x, y
#     if input == "R":
#         if x < a:
#             x += 1
#     elif input == "L":
#         if x > 1:
#             x -= 1
#     elif input == "U":
#         if y > 1:
#             y -= 1
#     elif input == "D":
#         if y < a:
#             y += 1
#
# a = int(sys.stdin.readline().rstrip())
# move_list = list(sys.stdin.readline().rstrip().split())
# size = len(move_list)
# x = 1
# y = 1
#
# for i in range(size):
#     move(move_list[i])
#
# print(y, x)

# 구현 알고리즘 예제 4-2번
# num = int(sys.stdin.readline().rstrip())
# count = 0
# for i in range(num+1):
#     for j in range(60):
#         for k in range(60):
#             if "3" in str(i) + str(j) + str(k):
#                 count+=1
#
# print(count)


#ICPC 신촌 캠프 대회
# 1 AC
# import sys
# digit = int(sys.stdin.readline().rstrip())
# binary = int(sys.stdin.readline().rstrip(), 2)
# division = int(sys.stdin.readline().rstrip())
# num = pow(2, division)
# # print(binary)
# # print(num)
# if binary % num == 0:
#     print("YES")
# else:
#     print('NO')


# 2 AC
# import sys
#
# num_people, card_num = map(int, sys.stdin.readline().rstrip().split())
# arr = []
# final = []
# final1 = []
# for i in range(num_people):
#     arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# for i in range(num_people):
#     for j in range(card_num):
#         final.append(arr[i][j])
#         final1.append(i+1)
# index = 0
# while len(final) > 1:
#
#     start = final[index]
#     final.pop(index)
#     final1.pop(index)
#     index += start - 1
#     index %= len(final)
#
# ans = final[0]
# ans1 = final1[0]
#
# print(ans1, ans)


# 3 미해결
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# arr = []
# for i in range(1, num+1):
#     arr.append(i)
#
# for i in range(num-1, 0, -1):
#     if arr[i-1] < arr[i]:
#         for j in range(num-1, 0, -1):
#             if arr[i-1] < arr[j]:
#                 arr[i-1], arr[j] = arr[j], arr[i-1]
#                 arr = arr[:i] + sorted(arr[i:])
#     check_arr = []
#     dp = [0] * num
#     dp[0] = arr[0]
#     check_arr.append(dp[0] % num)
#     for i in range(1, num):
#         dp[i] = dp[i - 1] + arr[i]
#         check_arr.append(dp[i] % num)
#         check_arr = list(set(check_arr))
#         if len(check_arr) >= ((num / 2) + 1): break
#
#     if len(check_arr) < ((num / 2) + 1):
#         print(*arr)
#         break
#
#     continue

#6 미해결
# import sys
# from collections import deque
# height, width = map(int, sys.stdin.readline().rstrip().split())
# world = []
# world_moves = []
# startY = 0
# startX = 0
# endY = 0
# endX = 0
# for i in range(height):
#     temp = list(sys.stdin.readline().rstrip())
#     world.append(temp)
#     world_moves.append([0]*len(temp))
#     if 'E' in temp:
#         endY = i
#         endX = temp.index('E')
#     if 'C' in temp:
#         startY = i
#         startX = temp.index('C')
#
# moveY = (-1, 1, 0, 0)
# moveX = (0, 0, -1, 1)
#
# def bfs(startY, startX):
#     queue = deque()
#     queue.append([startY, startX])
#     world_moves[startY][startX] = 1
#     while queue:
#         cur = queue.popleft()
#         for i in range(4):
#             tempY = cur[0] + moveY[i]
#             tempX = cur[1] + moveX[i]
#             if 0 <= tempY < height and 0 <= tempX < width:
#                 if world_moves[tempY][tempX] == 0:
#                     if world[tempY][tempX] != 'D':
#                         if world[tempY][tempX] == 'L':
#                             world_moves[tempY][tempX] = world_moves[cur[0]][cur[1]] + 5
#                             queue.append([tempY, tempX])
#                         if world[tempY][tempX] == 'X':
#
#
# bfs(startY, startX)
#
# print(world)
