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
#백준 2217번
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
#백준 2869번 달팽이는 올라가고 싶다
#
# import sys
#
# a, b, v = map(int, sys.stdin.readline().rstrip().split())
# if (v - a) % (a - b) != 0:
#     print(((v - a) // (a - b)) + 2)
# else:
#     print(((v - a) // (a - b)) + 1)

#백준 1929번 소수 구하기
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

#백준 2609번 최대공약수와 최소공배수
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

#백준 11650번 좌표 정렬하기
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

#백준 11651번 좌표 정렬하기2
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

#백준 2164 카드2
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

#백준 1920번 수찾기
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

#백준 7568번 덩치
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

#백준 10816번 숫자카드 2

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

#백준 1357 뒤집힌 덧셈
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

#백준 4949번 균형잡힌 세상
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

#백준 10814번 나이순 정렬
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

#백준 10773번 제로
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

#백준 1436번 영화감독 숌
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

#백준 10866번 덱
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

#백준 2108번 통계학
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

#백준 15829번 Hashing
# import sys
# num = int(sys.stdin.readline().rstrip())
# word_list = list(sys.stdin.readline().rstrip())
# total = 0
# for i in range(num):
#     total += (ord(word_list[i])-96) * (pow(31, i))
#
# print(total % 1234567891)

#백준 2775번 부녀회장이 될테야
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

#백준 1966번 프린터 큐
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

#백준 2231번 분해합
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
#백준 11866번 요세푸스 문제 0
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

#백준 1874번 스택 수열 틀림##############################################################
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

#백준 1874번 스택 수열 다른 방법
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

#백준 18111번 마인크래프트 시간 초과 구글링
#원래 했던 방식은 3중 for loop으로 n^3 시간 복잡도인데, counter를 사용해서 같은 블럭 높이를
#가지는 블럭들끼리 모아서 세고, 그걸 곱해서 forloop을 하나 빼는 방식을 사용하기 시간 초과가 안났다
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
#백준 1654번 랜선 자르기 이분탐색 매개변수탐색 구글링
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
#백준 2805번 나무 자르기 이분탐색 매개변수탐색 구글링
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

#백준 1463번 1로 만들기 다이나믹 프로그래밍 바텀업
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

#백준 2579번 계단 오르기 미해결
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# stairs = [0]
#
# cons = 0
# for i in range(num):
#     stairs.append(int(sys.stdin.readline().rstrip()))
#
# i = num
# stairs_point = stairs[num]
#
# while i != 0:
#     if i == 1:
#         i -= 1
#         break
#     if i == 2:
#         if cons == 1:
#             i -= 2
#         else:
#             i -= 2
#             stairs_point += stairs[i+1]
#     else:
#         if cons == 1:
#             i -= 2
#             stairs_point += stairs[i+2]
#             cons = 0
#         else:
#             if stairs[i-1] > stairs[i-2]:
#                 i -= 1
#                 stairs_point += stairs[i]
#                 cons = 1
#             else:
#                 i -= 2
#                 stairs_point += stairs[i]
#                 cons = 0
#
# print(stairs_point)

#백준 1260번 DFS와 BFS
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

#백준 1003번 피보나치 함수
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

#백준 11279번 최대 힙
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

#백준 1927번 최소 힙
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

#백준 11286번 절댓값 힙
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

#백준 1427번 소트인사이드
# import sys
#
# num = list(map(int, sys.stdin.readline().rstrip()))
#
# num.sort(reverse=True)
#
# for i in range(len(num)):
#     print(num[i], end = "")

#백준 17219번 비밀번호 찾기
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

#백준 9095번 1, 2, 3 더하기 다이나믹 프로그래밍 바텀업 미해결##################################
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# dp = [0, 1, 2, 3]
#
# def find():
#     #갯수찾기
#
# for i in range(num):
#     number = int(sys.stdin.readline().rstrip())

#백준 11659번 구간 합 구하기 4
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

#백준 7662번 이중 우선순위 큐 구글링
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

#백준 1676번 팩토리얼 0의 개수
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

#백준 11723번 집합
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

#백준 1620번 나는야 포켓몬 마스터 이다솜
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

#백준 1764번 듣보잡
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
# import sys
# num = int(sys.stdin.readline().rstrip())
# dp = [0] * 50001
# for i in range(1, 50001):
#     dp[i] = i*i

#백준 5525번 IOIOI
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
