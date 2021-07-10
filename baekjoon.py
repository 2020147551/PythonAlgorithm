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

#백준 1874번 다른 방법
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