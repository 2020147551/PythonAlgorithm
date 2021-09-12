# 백준 1541번 잃어버린 괄호 (2시간후 구글링)
# import sys
#
# working_list = list(sys.stdin.readline().rstrip().split("-"))
# num_list = []
# for i in working_list:
#     count = 0
#     a = i.split("+")
#     for j in a:
#         count += int(j)
#     num_list.append(count)
# total = int(num_list[0])
# for i in range(1, len(num_list)):
#     total -= num_list[i]
#
# print(total)
# 백준 2217번
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# rope_list = []
# max_weight = 0
# for i in range(num):
#     rope_list.append(int(sys.stdin.readline().rstrip()))
# rope_list.sort()
# index = 0
# for i in range(num):
#     temp = rope_list[i] * (num - i)
#     if temp > max_weight:
#         max_weight = temp
#
# print(max_weight)
# 백준 2869번 달팽이는 올라가고 싶다
#
# import sys
#
# a, b, v = map(int, sys.stdin.readline().rstrip().split())
# if (v - a) % (a - b) != 0:
#     print(((v - a) // (a - b)) + 2)
# else:
#     print(((v - a) // (a - b)) + 1)

# 백준 1929번 소수 구하기
# import sys
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# prime = [False] * (b+1)
#
# for i in range(2, b+1):
#     if prime[i] == False:
#         j = i * 2
#         while j <= b:
#             prime[j] = True
#             j += i
#
# for i in range(a, b+1):
#     prime[i] = not prime[i]
#
# if a > 2:
#     for i in range(a, b+1):
#         if prime[i]:
#             print(i)
# else:
#     for i in range(2, b+1):
#         if prime[i]:
#             print(i)

# 백준 2609번 최대공약수와 최소공배수
# import sys
#
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a,b):
#     return a*b / gcd(a, b)
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# print(int(gcd(a, b)))
# print(int(lcm(a, b)))

# 백준 10845번 큐
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# queue = []
# queue_size = 0
#
# def push(x):
#     global queue_size
#     global queue
#
#     queue.append(x)
#     queue_size += 1
#
#
# def pop():
#     global queue_size
#     global queue
#
#     if queue_size > 0:
#         queue_size -= 1
#         temp = queue[0]
#         queue.remove(queue[0])
#         return temp
#     else:
#         return -1
#
#
# step = ""
#
# for i in range(num):
#     step = sys.stdin.readline().rstrip()
#     if step[0:2] == "pu":
#         push(int(step[5:]))
#     elif step[0:2] == "po":
#         print(pop())
#     elif step[0:2] == "si":
#         print(queue_size)
#     elif step[0:2] == "em":
#         if queue_size == 0:
#             print(1)
#         else:
#             print(0)
#     elif step[0:2] == "fr":
#         if queue_size == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif step[0:2] == "ba":
#         if queue_size == 0:
#             print(-1)
#         else:
#             print(queue[-1])

# 백준 11650번 좌표 정렬하기
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# x_y_list = []
#
# for i in range(num):
#     x_y_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# x_y_list.sort(key=lambda x:(x[0], x[1]))
#
# for x, y in x_y_list:
#     print(x, y)

# 백준 11651번 좌표 정렬하기2
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# x_y_list = []
#
# for i in range(num):
#     x_y_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# x_y_list.sort(key=lambda x:(x[1], x[0]))
#
# for x, y in x_y_list:
#     print(x, y)

# 백준 2164 카드2
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
#
# card_list = deque()
# list_num = num
# for i in range(num):
#     card_list.append(i+1)
#
# while True:
#     if list_num == 1:
#         break
#     card_list.popleft()
#     list_num -= 1
#     card_list.append(card_list[0])
#     card_list.popleft()
#
# print(card_list[0])

# 백준 1920번 수찾기
# import sys
# from bisect import bisect_left, bisect_right
#
# def count_by_range(a, l, r):
#     right_index = bisect_right(a, r)
#     left_index = bisect_left(a, l)
#     return right_index - left_index
#
# size = int(sys.stdin.readline().rstrip())
#
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# find_size = int(sys.stdin.readline().rstrip())
#
# find_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# num_list.sort()
#
# for i in find_list:
#     temp = count_by_range(num_list, i, i)
#     if temp > 0:
#         print(1)
#     else:
#         print(0)

# 백준 7568번 덩치
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# pre_list = []
# people_list = []
# final_list = []
# for i in range(num):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     people_list.append([x, y])
#
# pre_list = people_list[:]
#
# people_list.sort(key = lambda x : x[0], reverse=True)
# list_bigger = []
# for i in range(num):
#     bigger = 0
#     for j in range(num):
#         if people_list[j][0] > pre_list[i][0] and people_list[j][1] > pre_list[i][1]:
#             bigger += 1
#         elif  people_list[j][0] > pre_list[i][0] and people_list[j][1] > pre_list[i][1]:
#             bigger += 1
#         else:
#             continue
#     list_bigger.append(bigger+1)
#
# for i in range(num):
#     print(list_bigger[i], end = " ")

# 백준 10816번 숫자카드 2

# import sys
# from bisect import bisect_left, bisect_right
#
# a_num = int(sys.stdin.readline().rstrip())
# a_list = list(map(int, sys.stdin.readline().rstrip().split()))
# a_list.sort()
# b_num = int(sys.stdin.readline().rstrip())
# b_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# def count_by_range(a_list, l, r):
#     right_index = bisect_right(a_list, r)
#     left_index = bisect_left(a_list, l)
#     return right_index - left_index
#
# for i in b_list:
#     print(count_by_range(a_list, i, i), end=" ")

# 백준 1357 뒤집힌 덧셈
# import sys
#
# def reverse(a):
#     a = a[::-1]
#     return int(a)
#
# a, b = sys.stdin.readline().rstrip().split()
#
# a = reverse(a)
# b = reverse(b)
#
# final = reverse(str(a+b))
#
# print(final)

# 백준 4949번 균형잡힌 세상
# import sys
#
# while True:
#     complete = True
#     stack = []
#     line = sys.stdin.readline().rstrip()
#     if line == ".":
#         break
#     for i in range(len(line)):
#         if line[i] == "(":
#             stack.append("(")
#         elif line[i] == "[":
#             stack.append("[")
#         elif line[i] == ")":
#             if len(stack) == 0:
#                 complete = False
#             elif stack.pop() != "(":
#                 complete = False
#         elif line[i] == "]":
#             if len(stack) == 0:
#                 complete = False
#             elif stack.pop() != "[":
#                 complete = False
#
#     if not complete or len(stack) != 0:
#         print("no")
#     else:
#         print("yes")

# 백준 10814번 나이순 정렬
#
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# people_list = []
#
# for i in range(num):
#     x, y = sys.stdin.readline().rstrip().split()
#     people_list.append([int(x), y])
#
# people_list.sort(key = lambda x : x[0])
#
# for i in range(num):
#     print(people_list[i][0], end = " ")
#     print(people_list[i][1])

# 백준 10773번 제로
#
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# stack = []
#
# total = 0
#
# for i in range(num):
#     temp = int(sys.stdin.readline().rstrip())
#     if temp != 0:
#         stack.append(temp)
#     else:
#         stack.pop()
#
# for i in range(len(stack)):
#     total += stack[i]
#
# print(total)

# 백준 1436번 영화감독 숌
#
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# arr = []
# i = 0
# while len(arr) < num:
#     i += 1
#     if "666" in str(i):
#         arr.append(i)
#
# print(arr[-1])

# 백준 10866번 덱
# import sys
# from collections import deque
# dq = deque()
# num = int(sys.stdin.readline().rstrip())
#
# for i in range(num):
#     oper = sys.stdin.readline().rstrip()
#     if oper[:2] == "pu":
#         operation, number = oper.split()
#         if operation == "push_front": dq.appendleft(number)
#         else: dq.append(number)
#     elif oper[:2] == "po":
#         if len(dq) == 0: print(-1)
#         else:
#             if oper == "pop_front": print(dq.popleft())
#             elif oper == "pop_back": print(dq.pop())
#     elif oper[:2] == "si": print(len(dq))
#     elif oper[:2] == "em":
#         if dq: print(0)
#         else: print(1)
#     elif oper[:2] == "fr":
#         if dq: print(dq[0])
#         else: print(-1)
#     elif oper[:2] == "ba":
#         if dq: print(dq[-1])
#         else: print(-1)

# 1018번 체스판 다시 칠하기 구글링####################################
# import sys
# n, m = map(int, sys.stdin.readline().rstrip().split())
# l = []
# mini = []
#
# for i in range(n):
#     l.append(sys.stdin.readline().rstrip())
#
# for a in range(n - 7):
#     for i in range(m - 7):
#         idx1 = 0
#         idx2 = 0
#         for b in range(a, a + 8):
#             for j in range(i, i + 8):
#                 if (j + b)%2 == 0:
#                     if l[b][j] != 'W': idx1 += 1
#                     if l[b][j] != 'B': idx2 += 1
#                 else :
#                     if l[b][j] != 'B': idx1 += 1
#                     if l[b][j] != 'W': idx2 += 1
#         mini.append(idx1)
#         mini.append(idx2)
#
# print(min(mini))

# 백준 2108번 통계학
# import sys
# from collections import Counter
# num = int(sys.stdin.readline().rstrip())
# num_list = []
#
# for i in range(num):
#     num_list.append(int(sys.stdin.readline().rstrip()))
#
# mean = 0
# for i in range(num):
#     mean += num_list[i]
#
# mean /= num
# print(round(mean))
#
# num_list.sort()
#
# if num % 2 == 1:
#     print(num_list[int((num+1)/2)-1])
# else:
#     print((num_list[int(num/2)-1] + num_list[int(num/2)])//2)
#
# def modefinder(num_list):
#     counter = Counter(num_list)
#     order = counter.most_common()
#     max = order[0][1]
#
#     mode = []
#     for i in order:
#         if i[1] == max:
#             mode.append(i[0])
#
#     return mode
#
# mode_list = modefinder(num_list)
#
# if len(mode_list) == 1:
#     print(mode_list[0])
# else:
#     print(mode_list[1])
#
# print(max(num_list) - min(num_list))

# 백준 15829번 Hashing
# import sys
# num = int(sys.stdin.readline().rstrip())
# word_list = list(sys.stdin.readline().rstrip())
# total = 0
# for i in range(num):
#     total += (ord(word_list[i])-96) * (pow(31, i))
#
# print(total % 1234567891)

# 백준 2775번 부녀회장이 될테야
# import sys
#
# test = int(sys.stdin.readline().rstrip())
#
# for i in range(test):
#     n = int(sys.stdin.readline().rstrip())
#     k = int(sys.stdin.readline().rstrip())
#     house = [[0] * k for _ in range(n+1)]
#     for i in range(k):
#         house[0][i] = i+1
#     for i in range(1, n+1):
#         house[i][0] = 1
#
#     for i in range(1, n+1):
#         for j in range(1, k):
#             house[i][j] = house[i-1][j] + house[i][j-1]
#     print(house[n][k-1])

# 백준 1966번 프린터 큐
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
# for i in range(num):
#     doc_num, doc_req = map(int, sys.stdin.readline().rstrip().split())
#     doc_index = deque()
#     order = 0
#     for i in range(doc_num):
#         doc_index.append(i)
#     if doc_num == 1:
#         pri = deque()
#         pri.append(int(sys.stdin.readline().rstrip()))
#     else:
#         pri = deque(map(int, sys.stdin.readline().rstrip().split()))
#
#     while True:
#         if len(pri) == 1:
#             pri.pop()
#             doc_index.pop()
#             order += 1
#             break
#
#         if pri[0] == max(pri):
#             temp_pri = pri.popleft()
#             temp_doc = doc_index.popleft()
#             order += 1
#             if temp_doc == doc_req:
#                 break
#
#         else:
#             pri.append(pri.popleft())
#             doc_index.append(doc_index.popleft())
#
#     print(order)

# 백준 2231번 분해합
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# total = 0
# for i in range(1, num + 1):
#     list_num = list(map(int, str(i)))
#     total = i + sum(list_num)
#
#     if total == num:
#         print(i)
#         break
#     elif i == num:
#         print(0)
#         break
# 백준 11866번 요세푸스 문제 0
# import sys
#
# n, k = map(int, sys.stdin.readline().rstrip().split())
# seq = []
# circle = []
# for i in range(1, n + 1):
#     circle.append(i)
#
# i = 0
# while True:
#     i += k-1
#     i %= len(circle)
#     seq.append(circle[i])
#     del circle[i]
#     if not circle: break
#
# print("<", end = "")
# for i in range(len(seq)-1):
#     print(seq[i], end = ", ")
# print(str(seq[len(seq)-1]) + ">")

# 백준 1874번 스택 수열 틀림##############################################################
# import sys
# num = int(sys.stdin.readline().rstrip())
# num_stack = []
# for i in range(num):
#     num_stack.append(i+1)
#
# num_stack.sort(reverse=True)
#
# wanted_list = []
#
# for i in range(num):
#     wanted_list.append(int(sys.stdin.readline().rstrip()))
#
# temp_stack = []
# result_stack = []
# oper_list = []
#
# for i in range(wanted_list[0]):
#         temp_stack.append(num_stack.pop())
#         oper_list.append("+")
#
# for i in wanted_list:
#     if len(num_stack) and i >= num_stack[-1]:
#         for j in range(i - num_stack[-1] + 1):
#             temp_stack.append(num_stack.pop())
#             oper_list.append("+")
#     if len(temp_stack) and i <= temp_stack[-1]:
#         for j in range(temp_stack[-1] - i + 1):
#             result_stack.append(temp_stack.pop())
#             oper_list.append("-")
#
# if result_stack == wanted_list:
#     for i in range(len(oper_list)):
#         print(oper_list[i])
# else:
#     print("NO")

# 백준 1874번 스택 수열 다른 방법
#
# import sys
# num = int(sys.stdin.readline().rstrip())
# temp_stack = []
# oper_list = []
# count = 0
# for i in range(num):
#     a = int(sys.stdin.readline().rstrip())
#     while count < a:
#         count += 1
#         temp_stack.append(count)
#         oper_list.append("+")
#
#     if temp_stack[-1] == a:
#         temp_stack.pop()
#         oper_list.append("-")
#     else:
#         print("NO")
#         oper_list = []
#         break
#
# for i in range(len(oper_list)):
#     print(oper_list[i])

# 백준 18111번 마인크래프트 시간 초과 구글링
# 원래 했던 방식은 3중 for loop으로 n^3 시간 복잡도인데, counter를 사용해서 같은 블럭 높이를
# 가지는 블럭들끼리 모아서 세고, 그걸 곱해서 forloop을 하나 빼는 방식을 사용하기 시간 초과가 안났다
# import sys
# from collections import Counter
#
# height, width, left_block = map(int, sys.stdin.readline().rstrip().split())
# world = []
# min_block = []
# max_block = []
# time = 999999999999999999999
# highest = 0
# for i in range(height):
#     line = map(int, sys.stdin.readline().rstrip().split())
#     world += line
#
# lowest = min(world)
# highest = max(world)
# land = dict(Counter(world))
#
# if highest > 256:
#     highest = 256
# for i in range(lowest, highest + 1):
#     time_taken = 0
#     usable_block = left_block
#     for key in land: #깎는거
#         if i < key:
#             install = (key - i) * land[key]
#             time_taken += 2 * install
#             usable_block += install
#     for key in land: #설치하는거
#         if i > key:
#             if usable_block >= (i - key) * land[key]:
#                 install = (i - key) * land[key]
#                 time_taken += install
#                 usable_block -= install
#             else:
#                 time_taken = 999999999999999999999
#                 break
#     if time_taken <= time:
#         time = time_taken
#         highest = i
#
# print(time, highest)
# 백준 1654번 랜선 자르기 이분탐색 매개변수탐색 구글링
# import sys
# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# line_list = []
#
# for i in range(a):
#     line_list.append(int(sys.stdin.readline().rstrip()))
#
# def search(start, end):
#     global line_list
#     line_num = 0
#     aver = int((start + end) / 2)
#     for i in range(len(line_list)):
#         line_num += int(line_list[i] // aver)
#
#     return line_num, aver
#
# start = 0
# end = max(line_list) + 1
# max_line = 0
# while True:
#     found_line, found_height = search(start, end)
#
#     if found_line < b:
#         end = found_height
#     elif found_line >= b:
#         if found_height > max_line:
#             max_line = found_height
#             start = found_height
#         else:
#             print(found_height)
#             break
# 백준 2805번 나무 자르기 이분탐색 매개변수탐색 구글링
# import sys
# a, b = map(int, sys.stdin.readline().rstrip().split())
# tree_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
#
# def search(aver):
#     length = sum(i - aver if i > aver else 0 for i in tree_list)
#
#     return length
#
#
# start = 0
# end = max(tree_list)
#
# while start <= end:
#     aver = (start + end)//2
#     found_length = search(aver)
#
#     if found_length >= b:
#         start = aver + 1
#     else:
#         end = aver - 1
#
# print(end)

# 백준 1463번 1로 만들기 다이나믹 프로그래밍 바텀업
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# num_arr = [0] * 1000001
#
# for i in range(2, num+1):
#     num_arr[i] = num_arr[i-1] + 1
#
#     if i % 2 == 0:
#         num_arr[i] = min(num_arr[i], num_arr[i//2] + 1)
#     if i % 3 == 0:
#         num_arr[i] = min(num_arr[i], num_arr[i//3] + 1)
#     if i % 6 == 0:
#         num_arr[i] = min(min(num_arr[i//3] + 1, num_arr[i//2] + 1) + 1, num_arr[i])
# print(num_arr[num])

# 백준 2579번 계단 오르기 구글링
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# stairs = [0] * 301
# dp = [0] * 301
#
# for i in range(1, num+1):
#     stairs[i] = int(sys.stdin.readline().rstrip())
#
# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
# dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
#
# for i in range(4, num+1):
#     dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
#
# print(dp[num])

# 백준 1260번 DFS와 BFS
#
# import sys
# from collections import deque
#
# ver, edge, start = map(int, sys.stdin.readline().rstrip().split())
#
# graph = [[] for _ in range(ver + 1)]
#
# for i in range(edge):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# for i in range(ver + 1):
#     graph[i].sort()
#
#
# stack_dfs = deque()
# stack_bfs = deque()
# visited_dfs = [False] * (ver + 1)
# visited_bfs = [False] * (ver + 1)
# order_dfs = []
# order_bfs = []
#
# def dfs(start):
#     stack_dfs.append(start)
#     visited_dfs[start] = True
#     print(start, end = " ")
#     for i in graph[start]:
#         if visited_dfs[i] == False:
#             dfs(i)
#
#     stack_dfs.pop()
#
# def bfs(start):
#     stack_bfs.append(start)
#     visited_bfs[start] = True
#     while stack_bfs:
#         temp = stack_bfs.popleft()
#         print(temp, end = " ")
#         for i in graph[temp]:
#             if visited_bfs[i] == False:
#                 stack_bfs.append(i)
#                 visited_bfs[i] = True
#
#
# dfs(start)
# print()
# bfs(start)

# 백준 1003번 피보나치 함수
# import sys
# num = int(sys.stdin.readline().rstrip())
# num_list = []
# fib_list = [[0, -1, -1] for _ in range(41)]
# fib_list[0] = [0, 1, 0]
# fib_list[1] = [1, 0, 1]
# for i in range(num):
#     num_list.append(int(sys.stdin.readline().rstrip()))
#
# def fibonacci(n):
#     global zero, one
#     if n == 0:
#         return fib_list[0]
#     if n == 1:
#         return fib_list[1]
#     if fib_list[n][0] != 0:
#         return fib_list[n]
#     nmin1 = fibonacci(n-1)
#     nmin2 = fibonacci(n-2)
#     fib_list[n][0] = nmin1[0] + nmin2[0]
#     fib_list[n][1] = nmin1[1] + nmin2[1]
#     fib_list[n][2] = nmin1[2] + nmin2[2]
#     return fib_list[n]
#
# for i in num_list:
#     fibonacci(i)
#     print(fib_list[i][1], fib_list[i][2])

# 백준 11279번 최대 힙
# import sys, heapq
#
# num = int(sys.stdin.readline().rstrip())
#
# max_heap = []
# result = []
# for i in range(num):
#     temp = int(sys.stdin.readline().rstrip())
#     if temp != 0:
#         heapq.heappush(max_heap, -temp)
#     else:
#         if len(max_heap) == 0:
#             print(0)
#         else:
#             print(-heapq.heappop(max_heap))

# 백준 1927번 최소 힙
# import sys, heapq
#
# num = int(sys.stdin.readline().rstrip())
#
# max_heap = []
# result = []
# for i in range(num):
#     temp = int(sys.stdin.readline().rstrip())
#     if temp != 0:
#         heapq.heappush(max_heap, temp)
#     else:
#         if len(max_heap) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(max_heap))

# 백준 11286번 절댓값 힙
# import sys, heapq
#
# num = int(sys.stdin.readline().rstrip())
#
# max_heap = []
# result = []
# for i in range(num):
#     temp = int(sys.stdin.readline().rstrip())
#     if temp != 0:
#         if temp < 0:
#             heapq.heappush(max_heap, (-temp, temp))
#         else:
#             heapq.heappush(max_heap, (temp, temp))
#     else:
#         if len(max_heap) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(max_heap)[1])

# 백준 1427번 소트인사이드
# import sys
#
# num = list(map(int, sys.stdin.readline().rstrip()))
#
# num.sort(reverse=True)
#
# for i in range(len(num)):
#     print(num[i], end = "")

# 백준 17219번 비밀번호 찾기
# import sys
# num, find = map(int, sys.stdin.readline().rstrip().split())
# pass_list = {}
# for i in range(num):
#     a, b = sys.stdin.readline().rstrip().split()
#     pass_list[a] = b
#
# for i in range(find):
#     link = sys.stdin.readline().rstrip()
#     print(pass_list[link])

# 백준 9095번 1, 2, 3 더하기
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# dp = [0, 1, 2, 4] + [0] * 7
#
# def find(x):
#     if dp[x] != 0:
#         return dp[x]
#     else:
#         if x == 1:
#             return find(1)
#         elif x == 2:
#             return find(2)
#         elif x == 3:
#             return find(3)
#         else:
#             return find(x-1) + find(x-2) + find(x-3)
# for i in range(num):
#     number = int(sys.stdin.readline().rstrip())
#     print(find(number))

# 백준 11659번 구간 합 구하기 4
# import sys
# num_size, num = map(int, sys.stdin.readline().rstrip().split())
#
# temp_list = list(map(int, sys.stdin.readline().rstrip().split()))
# num_list = [0]
# for i in range(num_size):
#     num_list.append(num_list[i] + temp_list[i])
#
#
# order_list = []
#
# for i in range(num):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     a -= 1
#     total = num_list[b] - num_list[a]
#     print(total)

# 백준 7662번 이중 우선순위 큐 구글링
# import sys
# import heapq
#
# number = int(sys.stdin.readline().rstrip())
#
# for i in range(number):
#     order_size = int(sys.stdin.readline().rstrip())
#     max_heap = []
#     max_heap_size = 0
#     min_heap = []
#     min_heap_size = 0
#     num_exist = [False] * 1000001
#
#     for i in range(order_size):
#         order, num = sys.stdin.readline().rstrip().split()
#         num = int(num)
#         if order == "I":
#             heapq.heappush(min_heap, (num, i))
#             min_heap_size += 1
#             heapq.heappush(max_heap, (-num, i))
#             max_heap_size += 1
#             num_exist[i] = True
#
#         elif order == "D":
#             if num < 0:
#                 while min_heap_size > 0 and not num_exist[min_heap[0][1]]:
#                     heapq.heappop(min_heap)
#                     min_heap_size -= 1
#                 if min_heap_size > 0:
#                     num_exist[min_heap[0][1]] = False
#                     heapq.heappop(min_heap)
#                     min_heap_size -= 1
#
#             else:
#                 while max_heap_size > 0 and not num_exist[max_heap[0][1]]:
#                     heapq.heappop(max_heap)
#                     max_heap_size -= 1
#                 if max_heap_size > 0:
#                     num_exist[max_heap[0][1]] = False
#                     heapq.heappop(max_heap)
#                     max_heap_size -= 1
#     while max_heap_size > 0 and not num_exist[max_heap[0][1]]:
#         heapq.heappop(max_heap)
#         max_heap_size -= 1
#     while min_heap_size > 0 and not num_exist[min_heap[0][1]]:
#         heapq.heappop(min_heap)
#         min_heap_size -= 1
#
#     if not max_heap_size or not min_heap_size:
#         print("EMPTY")
#     else:
#         print(-max_heap[0][0], min_heap[0][0])

# 백준 1676번 팩토리얼 0의 개수
# import sys
# num = int(sys.stdin.readline().rstrip())
#
# total = 1
#
# for i in range(2, num+1):
#     total *= i
#
# total_str = list(str(total))
# count = 0
# while total_str[-1] == "0":
#     total_str.pop()
#     count += 1
#
# print(count)

# 백준 11723번 집합
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# stack = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0}
#
# for i in range(num):
#     order = sys.stdin.readline().rstrip()
#     if order[0:3] == "all":
#         for j in range(1, 21):
#             stack[j] = 1
#     elif order[0:3] == "emp":
#         for j in range(1, 21):
#             stack[j] = 0
#     else:
#         order, value = order.split()
#         value = int(value)
#
#         if order == "add":
#             stack[value] = 1
#         elif order == "remove":
#             stack[value] = 0
#         elif order == "check":
#             print(stack[value])
#         elif order == "toggle":
#             if stack[value] == 0:
#                 stack[value] = 1
#             else:
#                 stack[value] = 0

# 백준 1620번 나는야 포켓몬 마스터 이다솜
# import sys
# pokemon_num, find_num = map(int, sys.stdin.readline().rstrip().split())
# pokedex_id = {}
# pokedex_name = {}
# for i in range(pokemon_num):
#     temp = sys.stdin.readline().rstrip()
#     pokedex_id[i] = temp
#     pokedex_name[temp] = i
# for i in range(find_num):
#     temp = sys.stdin.readline().rstrip()
#     if temp.isnumeric():
#         temp = int(temp)
#         print(pokedex_id[temp-1])
#     else:
#         print(pokedex_name[temp]+1)

# 백준 1764번 듣보잡
# import sys
# heard, seen = map(int, sys.stdin.readline().rstrip().split())
# people_list = {}
# count = 0
# for i in range(heard):
#     temp = sys.stdin.readline().rstrip()
#     people_list[temp] = 1
#
# for i in range(seen):
#     temp = sys.stdin.readline().rstrip()
#     try:
#         if people_list[temp] == 1:
#             people_list[temp] += 1
#             count += 1
#     except:
#         people_list[temp] = 1
#
# temp_list = {}
# for i in people_list.keys():
#     if people_list.get(i) == 2:
#         temp_list[i] = i
#
# sorted_list = sorted(temp_list)
# print(count)
# for i in range(count):
#     print(sorted_list[i])

# 백준 17626번 Four Squares 미해결
# 가장 큰 값으로 하는게 답이 아닐수도 있다... 어떻게 값을 구해야 하는지를 감을 못잡겠다
# import sys
# num = int(sys.stdin.readline().rstrip())
# dp = [0] * 50001
# count = 0
#
#
# def find(x):
#     i = 1
#     global count
#     while True:
#         if i * i > x:
#             x -= ((i-1)*(i-1))
#             count += 1
#             break
#         elif i * i == x:
#             x -= i*i
#             count += 1
#             break
#         i += 1
#     if x == 0:
#         return
#     else:
#         find(x)
# find(num)
# print(count)
# 백준 5525번 IOIOI
# import sys
# num = int(sys.stdin.readline().rstrip())
# length = int(sys.stdin.readline().rstrip())
#
# string = sys.stdin.readline().rstrip()
#
# count = 0
# cons = 0
# i = 1
# while i < length-1:
#     if string[i-1] == "I" and string[i] == "O" and string[i+1] == "I":
#         cons += 1
#         i += 1
#     else:
#         cons = 0
#     if cons == num:
#         count += 1
#         cons -= 1
#
#     i += 1
# print(count)

# 백준 9461번 파도반 수열
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# dp = [0, 1, 1, 1, 2, 2, 3, 4] + [0] * 95
#
# def findTri(x):
#     if dp[x] != 0:
#         return dp[x]
#     else:
#         dp[x] = findTri(x-1) + findTri(x-5)
#         return dp[x]
# for i in range(num):
#     n = int(sys.stdin.readline().rstrip())
#     print(findTri(n))

# 백준 5430번 AC
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
#
# for i in range(num):
#
#     order = list(sys.stdin.readline().rstrip())
#     size = int(sys.stdin.readline().rstrip())
#     num_arr = deque(list(sys.stdin.readline().rstrip().split(",")))
#
#     if size > 1:
#         num_arr[0] = num_arr[0][1:]
#         num_arr[-1] = num_arr[-1][:-1]
#
#     elif size == 1:
#         num_arr[0] = num_arr[0][1:-1]
#
#     else:
#         num_arr.pop()
#
#     try:
#         count = 0
#         for j in order:
#
#             if j == "R":
#                 count += 1
#
#             elif j == "D":
#                 if count % 2 == 0:
#                     num_arr.popleft()
#                     size -= 1
#                 else:
#                     num_arr.pop()
#                     size -= 1
#         if count % 2 == 0:
#             if size > 0:
#                 print("[", end="")
#                 for j in range(len(num_arr)-1):
#                     print(num_arr.popleft(), end = ",")
#                 print(num_arr.popleft() + "]")
#             else:
#                 print("[]")
#         else:
#             if size > 0:
#                 print("[", end="")
#                 for j in range(len(num_arr)-1):
#                     print(num_arr.pop(), end=",")
#                 print(num_arr.pop() + "]")
#             else:
#                 print("[]")
#
#     except:
#         print("error")
# 1475번 방번호
# import sys
#
# num = list(sys.stdin.readline().rstrip())
#
# single_set = [0] * 10
#
# for i in num:
#     if i == '0':
#         single_set[0] += 1
#     if i == '1':
#         single_set[1] += 1
#     if i == '2':
#         single_set[2] += 1
#     if i == '3':
#         single_set[3] += 1
#     if i == '4':
#         single_set[4] += 1
#     if i == '5':
#         single_set[5] += 1
#     if i == '6' or i == '9':
#         if single_set[6] > single_set[9]:
#             single_set[9] += 1
#         else:
#             single_set[6] += 1
#     if i == '7':
#         single_set[7] += 1
#     if i == '8':
#         single_set[8] += 1
#
#
#
# print(max(single_set))
# 1912번 연속합
#
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# dp = [0] * num
# dp[0] = num_list[0]
# i = 1
# while i < num:
#     if dp[i-1] > 0:
#         dp[i] = dp[i-1] + num_list[i]
#     else:
#         dp[i] = num_list[i]
#     i += 1
#
#
# print(max(dp))
#
# 11728번 배열 합치기
# import sys
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
# if a > 1:
#     a_list = list(map(int, sys.stdin.readline().rstrip().split()))
# else:
#     a_list = [int(sys.stdin.readline().rstrip())]
#
# if b > 1:
#     b_list = list(map(int, sys.stdin.readline().rstrip().split()))
# else:
#     b_list = [int(sys.stdin.readline().rstrip())]
#
# total_list = a_list + b_list
#
# total_list.sort()
# print(*total_list, end=" ")
# 10867 중복 뺴고 정렬하기
# import sys
# num = int(sys.stdin.readline().rstrip())
# arr = sorted(list(set(list(map(int, sys.stdin.readline().rstrip().split())))))
# print(*arr, end = " ")
# 11004 k번째 수
# import sys
# a, b = map(int, sys.stdin.readline().rstrip().split())
# num = sorted(list(map(int, sys.stdin.readline().rstrip().split())))[b-1]
# print(num)
# 10815번 숫자카드
# import sys, bisect
# a_num = int(sys.stdin.readline().rstrip())
# a_list = list(map(int, sys.stdin.readline().rstrip().split()))
# b_num = int(sys.stdin.readline().rstrip())
# b_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# a_list.sort()
#
# for i in b_list:
#     if bisect.bisect_left(a_list, i) == bisect.bisect_right(a_list, i):
#         print(0)
#     else:
#         print(1)

# 10826 피보나치 수 4
# import sys
# num = int(sys.stdin.readline().rstrip())
#
# dp = [0, 1, 1]
#
# for i in range(3, num+1):
#     dp.append(dp[i-1] + dp[i-2])
#
# print(dp[num])

# 2178 미로 탐색
# import sys
# from collections import deque
#
# height, width = map(int, sys.stdin.readline().rstrip().split())
# maze = []
# for i in range(height):
#     maze.append(list(map(int, sys.stdin.readline().rstrip())))
# #up down left right
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# queue = deque()
# visited = [[False] * width for _ in range(height)]
#
# def bfs(x, y):
#     queue.append([y, x])
#     visited[y][x] = True
#     while queue:
#         y, x = queue.popleft()
#
#         for i in range(4):
#             next_y = y + dy[i]
#             next_x = x + dx[i]
#             if next_y < 0 or next_x < 0 or next_y >= height or next_x >= width:
#                 continue
#             elif maze[next_y][next_x] == 0:
#                 continue
#             elif visited[next_y][next_x] == True:
#                 continue
#             maze[next_y][next_x] = maze[y][x] + 1
#             queue.append([next_y, next_x])
#             visited[next_y][next_x] = True
#     return maze[height-1][width-1]
# print(bfs(0, 0))
# 2667 단지번호붙이기
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
# maze = []
#
# for i in range(num):
#     maze.append(list(map(int, sys.stdin.readline().rstrip())))
#
# #up down left right
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# queue = deque()
# visited = [[False] * num for _ in range(num)]
# count = []
#
# def bfs(y, x):
#     count = 1
#     queue.append([y, x])
#     visited[y][x] = True
#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             next_y = y + dy[i]
#             next_x = x + dx[i]
#             if next_y < 0 or next_x < 0 or next_y >= num or next_x >= num:
#                 continue
#             elif maze[next_y][next_x] == 0:
#                 continue
#             elif visited[next_y][next_x] == True:
#                 continue
#             queue.append([next_y, next_x])
#             count += 1
#             visited[next_y][next_x] = True
#     return count
#
# for j in range(num):
#     for i in range(num):
#         if maze[j][i] == 1 and visited[j][i] == False:
#             count.append(bfs(j, i))
# print(len(count))
# count.sort()
# for i in range(len(count)):
#     print(count[i])

# 11724 연결 요소의 개수
# import sys
# from collections import deque
# node, edge = map(int, sys.stdin.readline().rstrip().split())
# connected = [[] for _ in range(node+1)]
# visited = [False] * (node+1)
# count = 0
# for i in range(edge):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     #since it's undirected graph, add both to each list to show that they are both connected
#     #to each other
#     connected[a].append(b)
#     connected[b].append(a)
#
# def bfs(start):
#     global count
#     if visited[start]: return #if it's visited, there's no need to check it again
#     else: count += 1 #if it's not visited, it means it's part of another connected component
#     queue = deque()
#     queue.append(start)
#     while queue:
#         cur = queue.popleft()
#         if not visited[cur]:
#             visited[cur] = True
#             for i in connected[cur]:
#                 queue.append(i)
#         else:
#             continue
# # print(connected)
# for i in range(1, node+1):
#     bfs(i)
#
# print(count)
# 11931번 수 정렬하기 4
# import sys
# num = int(sys.stdin.readline().rstrip())
# arr = []
# for i in range(num):
#     arr.append(int(sys.stdin.readline().rstrip()))
#
# arr.sort(reverse = True)
# for i in arr:
#     print(i)
# 2606 바이러스
# import sys
# from collections import deque
#
# num_comp = int(sys.stdin.readline().rstrip())
# num_conn = int(sys.stdin.readline().rstrip())
#
# arr = [[] for i in range(num_comp + 1)]
# visited = [False] * (num_comp + 1)
# for i in range(num_conn):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     arr[a].append(b)
#     arr[b].append(a)
#
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#
#     while queue:
#         cur = queue.popleft()
#         visited[cur] = True
#         for i in arr[cur]:
#             if not visited[i]:
#                 queue.append(i)
#
#
#
# bfs(1)
#
# count = 0
#
# for i in visited:
#     if i:
#         count += 1
#
# print(count-1)

# 7576번 토마토
# import sys
# from collections import deque
#
# x, y = map(int, sys.stdin.readline().rstrip().split())
#
# world = []
# for i in range(y):
#     world.append(list(map(int, sys.stdin.readline().rstrip().split())))
# startY = []
# startX = []
# for i in range(y):
#     for j in range(x):
#         if world[i][j] == 1:
#             startY.append(i)
#             startX.append(j)
#
# moveY = [-1, 1, 0, 0]
# moveX = [0, 0, -1, 1]
# count = 0
# def bfs():
#     queue = deque()
#     for i in range(len(startY)):
#         queue.append([startY[i], startX[i]])
#     while queue:
#         cur = queue.popleft()
#         for i in range(4):
#             tempY = cur[0] + moveY[i]
#             tempX = cur[1] + moveX[i]
#             if 0 <= tempX < x and 0 <= tempY < y:
#                 if world[tempY][tempX] != -1 and world[tempY][tempX] == 0:
#                     queue.append([tempY, tempX])
#                     world[tempY][tempX] = world[cur[0]][cur[1]] + 1
#
# bfs()
#
# maxnum = 0
# for i in range(y):
#     temp_max = max(world[i])
#     maxnum = max(temp_max, maxnum)
#     if 0 in world[i]:
#         maxnum = 999999999
# if maxnum == 999999999:
#     print(-1)
# else:
#     print(maxnum-1)
#
# 1012 유기농 배추
# import sys
# from collections import deque
# num = int(sys.stdin.readline().rstrip())
#
# def bfs(y, x):
#     global count
#     queue = deque()
#     if visited[y][x]:
#         return
#     queue.append([y, x])
#     count += 1
#     while queue:
#         cur = queue.popleft()
#         for i in range(4):
#             tempY = cur[0] + moveY[i]
#             tempX = cur[1] + moveX[i]
#             if 0 <= tempY < ySize and 0 <= tempX < xSize:
#                 if not visited[tempY][tempX]:
#                     if world[tempY][tempX] == 1:
#                         visited[tempY][tempX] = True
#                         queue.append([tempY, tempX])
#
# for i in range(num):
#     xSize, ySize, worm_count = map(int, sys.stdin.readline().rstrip().split())
#     world = [[0] * xSize for j in range(ySize)]
#     visited = [[False] * xSize for j in range(ySize)]
#
#     for k in range(worm_count):
#         a, b = map(int, sys.stdin.readline().rstrip().split())
#         world[b][a] = 1
#
#     moveY = [-1, 1, 0, 0]
#     moveX = [0, 0, -1, 1]
#     count = 0
#
#     for j in range(ySize):
#         for k in range(xSize):
#             if world[j][k] == 1:
#                 bfs(j, k)
#     print(count)
# 18870 좌표 압축
# import sys
# num = int(sys.stdin.readline().rstrip())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# sorted_arr = sorted(list(set(arr)))
# indices = {}
# for i in range(len(sorted_arr)):
#     indices[sorted_arr[i]] = i
#
# for i in arr:
#     print(indices[i], end = " ")
# 11726 2xn 타일링
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# dp = [0] * 1001
# dp[1] = 1
# dp[2] = 2
#
#
# def find(x):
#     if dp[x] != 0:
#         return dp[x]
#     dp[x] = find(x - 2) + find(x - 1)
#     return dp[x]
#
#
# print(find(num)%10007)
#
# 2630 색종이 만들기
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# blue = 0
# white = 0
#
# paper = []
# for i in range(num):
#     temp = list(map(int, sys.stdin.readline().rstrip().split()))
#     paper.append(temp)
#
#
# def divide(world):
#     global blue, white
#     half = len(world[0]) // 2
#     part1 = []
#     part2 = []
#     part3 = []
#     part4 = []
#     for i in range(half):
#         part1.append(world[i][:half])
#         part2.append(world[i][half:])
#         part3.append(world[half + i][:half])
#         part4.append(world[half + i][half:])
#     if part1 == part2 == part3 == part4 and check(part1):
#         color = part1[0][0]
#         if color == 1:
#             blue += 1
#         else:
#             white += 1
#     elif len(part1) == 1:
#         if part1[0][0] == 1:
#             blue += 1
#         else:
#             white += 1
#         if part2[0][0] == 1:
#             blue += 1
#         else:
#             white += 1
#         if part3[0][0] == 1:
#             blue += 1
#         else:
#             white += 1
#         if part4[0][0] == 1:
#             blue += 1
#         else:
#             white += 1
#     else:
#         divide(part1)
#         divide(part2)
#         divide(part3)
#         divide(part4)
#
#
# def check(world):
#     temp = []
#     if len(world[0]) == 2:
#         if world[0][0] == world[0][1] == world[1][0] == world[1][1]:
#             return True
#         return False
#     if len(world[0]) == 1:
#         return True
#     for i in range(len(world[0])//2):
#         temp.append(world[i][:len(world[0])//2])
#     return check(temp)
#
#
# divide(paper)
#
# print(white)
# print(blue)

# 1931 회의실 배정
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# list_time = []
# for i in range(num):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     list_time.append([a, b])
#
# list_time.sort(key=lambda x: (x[1], x[0]))
#
# count = 0
# end = 0
#
# for i in list_time:
#     if end <= i[0]:
#         end = i[1]
#         count += 1
#
# print(count)
#
# print(*list_time)
#
# 10026 Cow Art
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
#
# painting = []
# human_visited = [[False] * num for i in range(num)]
# cow_visited = [[False] * num for i in range(num)]
# human_count = 0
# cow_count = 0
# for i in range(num):
#     temp = list(sys.stdin.readline().rstrip())
#     painting.append(temp)
#
# moveY = [-1, 1, 0, 0]
# moveX = [0, 0, -1, 1]
#
# def human_bfs(startY, startX):
#     global human_count
#     queue = deque()
#     queue.append([startY, startX])
#     human_visited[startY][startX] = True
#     human_count += 1
#     while queue:
#         cur = queue.popleft()
#         for i in range(4):
#             tempY = cur[0] + moveY[i]
#             tempX = cur[1] + moveX[i]
#
#             if 0 <= tempY < len(painting) and 0 <= tempX < len(painting):
#                 if not human_visited[tempY][tempX]:
#                     if painting[cur[0]][cur[1]] == painting[tempY][tempX]:
#                         human_visited[tempY][tempX] = True
#                         queue.append([tempY, tempX])
#
# def cow_bfs(startY, startX):
#     global cow_count
#     queue = deque()
#     queue.append([startY, startX])
#     cow_visited[startY][startX] = True
#     cow_count += 1
#     while queue:
#         cur = queue.popleft()
#         for i in range(4):
#             tempY = cur[0] + moveY[i]
#             tempX = cur[1] + moveX[i]
#
#             if 0 <= tempY < len(painting) and 0 <= tempX < len(painting):
#                 if not cow_visited[tempY][tempX]:
#                     color = painting[cur[0]][cur[1]]
#                     if color == "R" or color == "G":
#                         if painting[tempY][tempX] == 'R' or painting[tempY][tempX] == 'G':
#                             cow_visited[tempY][tempX] = True
#                             queue.append([tempY, tempX])
#                     else:
#                         if color == painting[tempY][tempX]:
#                             cow_visited[tempY][tempX] = True
#                             queue.append([tempY, tempX])
#
#
#
# for i in range(num): #y
#     for j in range(num): #x
#         if not human_visited[i][j]:
#             human_bfs(i, j)
#         if not cow_visited[i][j]:
#             cow_bfs(i, j)
#
# print(human_count, cow_count)
#
# 10211 Maximum subarray
# import sys
# num = int(sys.stdin.readline().rstrip())
# for i in range(num):
#     length = int(sys.stdin.readline().rstrip())
#     arr = list(map(int, sys.stdin.readline().rstrip().split()))
#     max_num = -99999999
#     for j in range(length):
#         if j > 0:
#             if arr[j-1] >= 0:
#                 arr[j] += arr[j-1]
#         max_num = max(arr[j], max_num)
#     print(max_num)

# 17626 Four Squares 구글링, 도저히 방법을 못떠올림
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# dp = [0] * (num+1)
# dp[0] = 0
# dp[1] = 1
# for i in range(2, num+1):
#     minVal = 999999999
#     j = 1
#     while (j**2) <= i:
#         minVal = min(minVal, dp[i-(j**2)])
#         j += 1
#     dp[i] = minVal + 1
#
# print(dp[num])

# 7569 토마토
# import sys
# from collections import deque
# sizeX, sizeY, height = map(int, sys.stdin.readline().rstrip().split())
# days = 0
# able = True
# tomatoes = [[] for i in range(height)]
# cases = []
# for i in range(sizeY * height):
#     cur = i // sizeY
#     line = list(map(int, sys.stdin.readline().rstrip().split()))
#     tomatoes[cur].append(line)
#
# moveY = [-1, 1, 0, 0, 0, 0] #2d 상하
# moveX = [0, 0, -1, 1, 0, 0] #2d 좌우
# moveZ = [0, 0, 0, 0, 1, -1] #3d 상하
#
#
# def bfs():
#     global days
#     queue = deque()
#     for i in cases:
#         queue.append(i) #z, y, x
#     while queue:
#         cur = queue.popleft()
#         for i in range(6):
#             tempY = cur[1] + moveY[i]
#             tempX = cur[2] + moveX[i]
#             tempZ = cur[0] + moveZ[i]
#             if 0 <= tempY < sizeY and 0 <= tempX < sizeX and 0 <= tempZ < height:
#                 if tomatoes[tempZ][tempY][tempX] == 0:
#                     queue.append([tempZ, tempY, tempX])
#                     tomatoes[tempZ][tempY][tempX] = tomatoes[cur[0]][cur[1]][cur[2]] + 1
#                     days = max(days, tomatoes[cur[0]][cur[1]][cur[2]])
#
# for i in range(height):
#     for j in range(sizeY):
#         for k in range(sizeX):
#             if tomatoes[i][j][k] == 1:
#                 cases.append([i, j, k])
#
# bfs()
#
# while able:
#     for i in range(height):
#         for j in range(sizeY):
#             if 0 in tomatoes[i][j]:
#                 able = False
#                 break
#         if not able:
#             break
#     if able:
#         break
#
# if able:
#     print(days)
# else:
#     print(-1)

# 16928 뱀과 사다리 게임
# import sys
# from collections import deque
# ladder, snake = map(int, sys.stdin.readline().rstrip().split())
#
# ladder_list_start = []
# ladder_list_end = []
# snake_list_start = []
# snake_list_end = []
# board = [0] * 101
# visited = [False] * 101
# turns = 0
#
# for i in range(ladder):
#     start, end = map(int, sys.stdin.readline().rstrip().split())
#     ladder_list_start.append(start)
#     ladder_list_end.append(end)
#
# for i in range(snake):
#     start, end = map(int, sys.stdin.readline().rstrip().split())
#     snake_list_start.append(start)
#     snake_list_end.append(end)
# def bfs():
#     queue = deque()
#     queue.append(1)
#     visited[1] = True
#     while queue:
#         cur = queue.popleft()
#         if cur == 100:
#             return
#         for i in range(1, 7):
#             temp = cur + i
#             if 1 <= temp <= 100:
#                 if not visited[temp]:
#                     if temp in ladder_list_start:
#                         index = ladder_list_start.index(temp)
#                         temp = ladder_list_end[index]
#                         if board[temp] == 0:
#                             board[temp] = board[cur] + 1
#                         else:
#                             board[temp] = min(board[cur] + 1, board[temp])
#                         queue.append(temp)
#                         visited[temp] = True
#                     elif temp in snake_list_start:
#                         index = snake_list_start.index(temp)
#                         temp = snake_list_end[index]
#                         if board[temp] == 0:
#                             board[temp] = board[cur] + 1
#                         else:
#                             board[temp] = min(board[cur] + 1, board[temp])
#                         queue.append(temp)
#                         visited[temp] = True
#                     else:
#                         if board[temp] == 0:
#                             board[temp] = board[cur] + 1
#                         else:
#                             board[temp] = min(board[cur] + 1, board[temp])
#                         queue.append(temp)
#                         visited[temp] = True
#
# bfs()
#
# print(board[100])

# 1389 케빈 베이컨의 6단계 법칙
# import sys
# from collections import deque
# people, connection = map(int, sys.stdin.readline().rstrip().split())
# conn = [[] for i in range(people + 1)]
# total_arr = []
#
# for i in range(connection):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     conn[a].append(b)
#     conn[b].append(a)
#
#
# def bfs(start):
#     visited = [0] * (people + 1)
#     visited_bool = [False] * (people + 1)
#     queue = deque()
#     queue.append(start)
#     while queue:
#         cur = queue.popleft()
#         for j in conn[cur]:
#             if not visited_bool[j]:
#                 if j == start:
#                     continue
#                 if visited[j] == 0:
#                     visited[j] = visited[cur] + 1
#                 else:
#                     visited[j] = min(visited[cur] + 1, visited[j])
#                 queue.append(j)
#                 visited_bool[j] = True
#     return visited
#
#
# for i in range(1, people + 1):
#     total_arr.append([sum(bfs(i)), i])
#
# total_arr.sort(key=lambda x: x[0])
#
# print(total_arr[0][1])

# 11403 경로찾기 미해결
# import sys
# size = int(sys.stdin.readline().rstrip())
#
# arr = []
# for i in range(size):
#     arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
#

# 9375 Incognito
# import sys
#
# test_case = int(sys.stdin.readline().rstrip())
#
# for i in range(test_case):
#     num = int(sys.stdin.readline().rstrip())
#     dic = {}
#     for j in range(num):
#         name, type = sys.stdin.readline().rstrip().split()
#         if type in dic.keys():
#             dic[type].append(name)
#         else:
#             dic[type] = list()
#             dic[type].append(name)
#     ans = 1
#     for j in dic.keys():
#         ans *= (len(dic[j])+1)
#
#     print(ans-1)

# 1780 종이의 개수
# import sys
# num = int(sys.stdin.readline().rstrip())
#
# paper = []
# count1 = 0
# count2 = 0
# count3 = 0
#
# for i in range(num):
#     paper.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# def divide(paper):
#     global count1, count2, count3
#     divided = [[] for j in range(9)]
#     first = len(paper[0]) // 3
#     second = first * 2
#     for j in range(0, len(paper[0])//3):
#         divided[0].append(paper[j][:first])
#         divided[1].append(paper[j][first:second])
#         divided[2].append(paper[j][second:])
#         divided[3].append(paper[j+first][:first])
#         divided[4].append(paper[j+first][first:second])
#         divided[5].append(paper[j+first][second:])
#         divided[6].append(paper[j + second][:first])
#         divided[7].append(paper[j + second][first:second])
#         divided[8].append(paper[j + second][second:])
#
#     equal = True
#
#     for j in range(1, len(divided)):
#         if divided[0] != divided[j]:
#             equal = False
#             break
#
#     if equal and check(divided):
#         paper_type = divided[0][0][0]
#         if paper_type == -1:
#             count1 += 1
#         elif paper_type == 0:
#             count2 += 1
#         elif paper_type == 1:
#             count3 += 1
#
#
#     elif len(divided[0]) == 1:
#         for j in range(9):
#             if divided[j][0][0] == -1:
#                 count1 += 1
#             elif divided[j][0][0] == 0:
#                 count2 += 1
#             else:
#                 count3 += 1
#
#     else:
#         for j in range(len(divided)):
#             divide(divided[j])
#
# def check(paper):
#     # first = len(paper[0])//3
#     # second = first * 2
#     if paper[0] == paper[1] == paper[2]:
#         for k in range(1, len(paper[0])):
#             if paper[0][0] != paper[0][k]:
#                 return False
#         return True
#     return False
#
#
# divide(paper)
# print(count1)
# print(count2)
# print(count3)
#
# 11727 2xn 타일링 2

# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# dp = [0] * 1001
# dp[1] = 1
# dp[2] = 3
#
# def find(num):
#     if dp[num] != 0:
#         return dp[num]
#     if num == 2:
#         return dp[2]
#     if num == 1:
#         return dp[1]
#     dp[num] = find(num-1) + 2*find(num-2)
#     return dp[num]
#
# print(find(num)%10007)

# 11403 경로 찾기
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
#
# arr = []
# ans_arr = []
#
# for i in range(num):
#     temp = list(map(int, sys.stdin.readline().rstrip().split()))
#     arr.append(temp)
#     ans_arr.append([0] * len(temp))
#
# # for i in range(num):
# #     for j in range(num):
# #         if i != j and arr[i][j] == 0:
# #             arr[i][j] = 999999999
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     while queue:
#         cur = queue.popleft()
#         for k in range(len(arr[cur])):
#             if arr[cur][k] and not ans_arr[start][k]:
#                 ans_arr[start][k] = 1
#                 queue.append(k)
#
# for i in range(num):
#     bfs(i)
#
# for i in range(num):
#     for j in range(num):
#         print(ans_arr[i][j], end = " ")
#
#     print()

# 6064 cain calendar
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# for i in range(num):
#     m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
#     sets = [1, 1]
#     count = 1
#     if sets[0] != x:
#         temp = x - sets[0]
#         sets[0] += temp
#         sets[1] += temp
#         count += temp
#
#     if sets[1] > n:
#         sets[1] = sets[1] % n
#         if sets[1] == 0:
#             sets[1] = n
#
#     if sets[0] == x and sets[1] == y:
#         print(count)
#         continue
#
#     temp1 = x
#     temp2 = m - x
#     while True:
#         sets[0] += temp2
#         sets[1] += temp2
#         count += temp2
#         if sets[0] > m:
#             sets[0] = sets[0] - m
#
#         if sets[1] > n:
#             sets[1] = sets[1] % n
#             if sets[1] == 0:
#                 sets[1] = n
#
#         if sets[0] == m and sets[1] == n:
#             print(-1)
#             break
#
#         sets[0] += temp1
#         sets[1] += temp1
#         count += temp1
#         if sets[0] > m:
#             sets[0] = sets[0] - m
#
#         if sets[1] > n:
#             sets[1] = sets[1] % n
#             if sets[1] == 0:
#                 sets[1] = n
#
#         if sets[0] == x and sets[1] == y:
#             print(count)
#             break
#
# 14500 테트리미노
# import sys
#
# y, x = map(int, sys.stdin.readline().rstrip().split())
#
# main_arr = []
# max_sum = 0
# for i in range(y):
#     main_arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
#
# def check(arr):
#     global max_sum
#     for i in range(5):
#         for j in range(y):
#             for k in range(x):
#                 if i == 0:
#                     try:
#                         temp = 0
#                         temp += arr[j][k]
#                         temp += arr[j + 1][k]
#                         temp += arr[j + 2][k]
#                         temp += arr[j + 3][k]
#
#                         max_sum = max(max_sum, temp)
#                     except:
#                         continue
#                 elif i == 1:
#                     try:
#                         temp = 0
#                         temp += arr[j][k]
#                         temp += arr[j + 1][k]
#                         temp += arr[j][k+1]
#                         temp += arr[j+1][k+1]
#
#                         max_sum = max(max_sum, temp)
#                     except:
#                         continue
#                 elif i == 2:
#                     try:
#                         temp = 0
#                         temp += arr[j][k]
#                         temp += arr[j + 1][k]
#                         temp += arr[j + 2][k]
#                         temp += arr[j + 2][k + 1]
#
#                         max_sum = max(max_sum, temp)
#                     except:
#                         continue
#                 elif i == 3:
#                     try:
#                         temp = 0
#                         temp += arr[j][k]
#                         temp += arr[j+1][k]
#                         temp += arr[j+1][k+1]
#                         temp += arr[j+2][k+1]
#
#                         max_sum = max(max_sum, temp)
#                     except:
#                         continue
#                 else:
#                     try:
#                         temp = 0
#                         temp += arr[j][k]
#                         temp += arr[j][k+1]
#                         temp += arr[j][k+2]
#                         temp += arr[j+1][k+1]
#
#                         max_sum = max(max_sum, temp)
#                     except:
#                         continue
#
# def rotated(array_2d):
#     list_of_tuples = zip(*array_2d[::-1])
#     return [list(elem) for elem in list_of_tuples]
#
# def flipped(array_2d):
#     temp = []
#     for i in array_2d:
#         temp.append(i[::-1])
#     return temp
# for i in range(4):
#     check(main_arr)
#     main_arr = rotated(main_arr)
#     x, y = y, x
#
# main_arr = flipped(main_arr)
#
# for i in range(4):
#     check(main_arr)
#     main_arr = rotated(main_arr)
#     x, y = y, x
#
#
# print(max_sum)


# 1992 쿼드트리
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# array = []
# ans = ''
# for i in range(num):
#     array.append(list(map(int, sys.stdin.readline().rstrip())))
#
# def check(arr):
#     global ans
#     length = len(arr)
#     part1 = []
#     part2 = []
#     part3 = []
#     part4 = []
#     for i in range(len(arr)//2):
#         part1.append(arr[i][:length//2])
#         part2.append(arr[i][length//2:])
#         part3.append(arr[length//2 + i][:length//2])
#         part4.append(arr[length//2 + i][length//2:])
#
#     if part1 == part2 == part3 == part4 and verify(part1):
#         ans += str(part1[0][0])
#     elif len(part1) == 1:
#         ans += '('
#         ans += str(part1[0][0])
#         ans += str(part2[0][0])
#         ans += str(part3[0][0])
#         ans += str(part4[0][0])
#         ans += ')'
#     else:
#         ans += ('(')
#         check(part1)
#         check(part2)
#         check(part3)
#         check(part4)
#         ans += (')')
#
# def verify(arr):
#     temp = []
#     if len(arr[0]) == 1:
#         return True
#     elif len(arr[0]) == 2:
#         if arr[0][0] == arr[0][1] == arr[1][0] == arr[1][1]:
#             return True
#         return False
#     for i in range(len(arr[0])//2):
#         temp.append(arr[i][:len(arr[0])//2])
#     return verify(temp)
#
# check(array)
#
# print(ans)

# 1107 리모컨
# import sys
#
#
# desired_channel = sys.stdin.readline().rstrip()
# digit = len(desired_channel)
# disabled_num = int(sys.stdin.readline().rstrip())
#
# disabled_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# from_begin = abs(100 - int(desired_channel))
#
# upper_num = 999999
# lower_num = -999999
# num = 0
#
# if disabled_num == 10:
#     print(from_begin)
#     exit()
#
# if disabled_num == 0:
#     print(min(from_begin, digit))
#     exit()
#
# while num <= int(desired_channel): #find lower bound number
#     able = True
#     temp = []
#     num_list = list(str(num))
#     for i in num_list:
#         if int(i) in disabled_list:
#             able = False
#             break
#     if able and num > lower_num:
#         lower_num = num
#     num += 1
#
# num = 999999
#
# while num >= int(desired_channel):
#     able = True
#     temp = []
#     num_list = list(str(num))
#     for i in num_list:
#         if int(i) in disabled_list:
#             able = False
#             break
#     if able and num < upper_num:
#         upper_num = num
#     num -= 1
#
# upper_num_2 = abs(int(desired_channel) - upper_num)
# lower_num_2 = abs(int(desired_channel) - lower_num)
#
# print(min(upper_num_2 + len(str(upper_num)), lower_num_2 + len(str(lower_num)), from_begin))

# 9019 DSLR
# import sys
# from collections import deque
# test_case = int(sys.stdin.readline().rstrip())
#
#
# def bfs(start, end):
#     global temp
#     visited = [False] * 10001
#     queue = deque()
#     queue.append([start, ''])
#     visited[start] = True
#     while queue:
#         cur = queue.popleft()
#         for i in range(4):
#             string = cur[1]
#             if i == 0:
#                 temp = cur[0] * 2
#                 if temp > 9999:
#                     temp %= 10000
#                 string += 'D'
#             elif i == 1:
#                 temp = cur[0] - 1
#                 if cur[0] == 0:
#                     temp = 9999
#                 string += 'S'
#             elif i == 2:
#                 temp = (cur[0] % 1000) * 10 + (cur[0]//1000)
#                 string += 'L'
#             elif i == 3:
#                 temp = (cur[0] % 10) * 1000 + (cur[0]//10)
#                 string += 'R'
#             if temp == end:
#                 return string
#             elif temp != end and not visited[temp]:
#                 visited[temp] = True
#                 queue.append([temp, string])
#
#
# for _ in range(test_case):
#     initial_num, final_num = map(int, sys.stdin.readline().rstrip().split())
#     print(bfs(initial_num, final_num))
#
# 16236 아기 상어
import sys
from copy import deepcopy
from collections import deque
import heapq

size = int(sys.stdin.readline().rstrip())
fish_size = 2
eaten = 0
time = 0
moved = 0
array = []
visited = []

startY = 0
startX = 0
for i in range(size):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    if 9 in temp:
        startY = i
        startX = temp.index(9)
    array.append(temp)
    visited.append([False] * len(temp))
new_visited = deepcopy(visited)
moveY = [-1, 0, 0, 1]
moveX = [0, -1, 1, 0]


def bfs(y, x, a, b, c, d):  # 먹은 위치만 visited 처리해주면 된다
    global visited, time, fish_size, eaten, moved
    queue = deque()
    queue.append([y, x, a, b, c, d])
    while True:
        edible = []
        while queue:
            cur = queue.popleft()
            for i in range(4):
                tempY = cur[0] + moveY[i]
                tempX = cur[1] + moveX[i]
                fish_size = cur[2]
                eaten = cur[3]
                time = cur[4]
                moved = cur[5] + 1
                if 0 <= tempY < size and 0 <= tempX < size and not visited[tempY][tempX]:
                    if array[tempY][tempX] < fish_size and array[tempY][tempX] != 0:
                        if edible:
                            if moved == edible[0][5]:
                                heapq.heappush(edible, [tempY, tempX, fish_size, eaten, time, moved])
                        else:
                            heapq.heappush(edible, [tempY, tempX, fish_size, eaten, time, moved])
                    if not edible:
                        if array[tempY][tempX] == fish_size or array[tempY][tempX] == 0 or array[tempY][tempX] == 9:
                            queue.append([tempY, tempX, fish_size, eaten, time, moved])
                            visited[tempY][tempX] = True
                        else:
                            visited[tempY][tempX] = True
        if edible:
            return edible[0]
        else:
            return False


while True:
    result = bfs(startY, startX, fish_size, eaten, time, moved)

    if result:
        startY = result[0]
        startX = result[1]
        fish_size = result[2]
        eaten = result[3] + 1
        time = result[4] + result[5]
        moved = 0
        if eaten == fish_size:
            eaten = 0
            fish_size += 1
        array[startY][startX] = 0
        visited = deepcopy(new_visited)
    else:
        break

print(time)
