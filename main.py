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

#
# import sys
#
# node, edge = map(int, sys.stdin.readline().rstrip().split())
# edges = []
#
# graph = dict([])
#
#
# def find(graph):
#     if len(graph) == 0:
#         return []
#     if len(graph) == 1:
#         return [list(graph.keys())[0]]
#     vCurrent = list(graph.keys())[0]
#     graph2 = dict(graph)
#
#     del graph2[vCurrent]
#
#     res1 = find(graph2)
#
#     for v in graph[vCurrent]:
#         if v in graph2:
#             del graph2[v]
#
#     res2 = [vCurrent] + find(graph2)
#
#     if len(res1) > len(res2):
#         return res1
#     return res2
#
# for i in range(edge):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     if a not in graph:
#         graph[a] = []
#     if b not in graph:
#         graph[b] = []
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# maxSet = find(graph)
#
# print(len(maxSet))
# maxSet.sort()
# print(*maxSet)

#SUAPC F번
# import sys
# test_case = int(sys.stdin.readline().rstrip())
#
# for i in range(test_case):
#     n, k = map(int, sys.stdin.readline().rstrip().split())
#     each = 4
#     start = 0
#
#
#     print(start)
#
#

#SUAPC H번
# import sys
# import heapq
# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
#
# heapq.heapify(arr)
# count = 0
# i = 0
# while arr:
#     x = heapq.heappop(arr)
#     if x == b:
#         count += 1
#         if len(arr) == 0:
#             break
#         x = heapq.heappop(arr)
#     if len(arr) == 0:
#         break
#     y = heapq.heappop(arr)
#     if y == b:
#         count += 1
#         if len(arr) == 0:
#             break
#         y = heapq.heappop(arr)
#     temp = x + y
#     if temp < b:
#         temp += (b/2)
#         if temp >= b:
#             count += 1
#         else:
#             heapq.heappush(arr, temp)
#     else:
#         count += 1
#
# print(count)
