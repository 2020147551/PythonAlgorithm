# ICPC 신촌 캠프 Lecture 1 출석 문제 및 연습 문제

# 15552 빠른 A+B

# import sys
# number = int(input())
#
# for a in range(number):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A + B)

# 10804 카드 역배치

# import sys
#
# card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# for i in range(10):
#
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     a -= 1
#     b -= 1
#     if (b + 1 - a) % 2 == 0:
#         times = (b + 1 - a) // 2
#     else:
#         times = ((b + 1 - a) - 1) // 2
#
#     for i in range(1, times + 1):
#         temp = card_list[a]
#         card_list[a] = card_list[b]
#         card_list[b] = temp
#         a += 1
#         b -= 1
#
# for i in range(len(card_list)):
#     print(card_list[i], end = " ")

# 1158 요세푸스 문제

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

# 1547 공 문제

# import sys
#
# count = int(sys.stdin.readline().rstrip())
#
# cup_list = ["1", "2", "3"]
#
# for i in range(count):
#     x, y = sys.stdin.readline().rstrip().split()
#     a, b = cup_list.index(x), cup_list.index(y)
#     cup_list[b] = x
#     cup_list[a] = y
#
# print(cup_list[0])

# 9093 단어 뒤집기

# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# for i in range(num):
#     word_list = sys.stdin.readline().rstrip().split()
#     for j in range(len(word_list)):
#         word_list[j] = word_list[j][::-1]
#         print(word_list[j], end = " ")

# 2346 풍선 터뜨리기

# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# bal_list = list(map(int, sys.stdin.readline().rstrip().split()))
# bal_index = []
# for i in range(num):
#     bal_index.append(i)
# seq = []
# cur = 0
# for i in range(1, num+1):
#     step = bal_list[cur]
#     del bal_list[cur]
#     seq.append(bal_index[cur]+1)
#     del bal_index[cur]
#     if cur < 0:
#         cur += 1
#     if step > 0:
#         cur += step-1
#     else:
#         cur += step
#     if cur > 0 and len(bal_list) > 0:
#         cur %= len(bal_list)
#     elif cur < 0 and len(bal_list) > 0:
#         cur *= -1
#         cur %= len(bal_list)
#         cur *= -1
#
# for i in range(num):
#     print(seq[i], end=" ")

# ICPC 신촌 캠프 Lecture 2 출석 문제 및 연습 문제

# 10825 국영수
# import sys
#
# num = int(sys.stdin.readline().rstrip())
# grade_list = []
#
# for i in range(num):
#     name, lang, eng, math = sys.stdin.readline().rstrip().split()
#     grade_list.append([int(lang), int(eng), int(math), name])
#
# grade_list.sort(key = lambda x : (-x[0], x[1], -x[2], x[3]))
#
# for i in range(num):
#     print(grade_list[i][3])
#
# 10610 30
# import sys
# num = list(sys.stdin.readline().rstrip())
# num.sort(reverse=True)
# string = [str(a) for a in num]
# num_string = "".join(string)
# integer = int(num_string)
#
# if integer % 30 == 0:
#     print(integer)
# else:
#     print(-1)

# 2437 저울
# import sys
# num = int(sys.stdin.readline().rstrip())
# weight_list = list(map(int, sys.stdin.readline().rstrip().split()))
# weight_list.sort()
#
# total = 1
#
# for i in weight_list:
#     if total < i:
#         break
#     total += i
#
# print(total)

# 1448 삼각형 만들기
# import sys
# num = int(sys.stdin.readline().rstrip())
#
# straw_list = []
#
# for i in range(num):
#     straw_list.append(int(sys.stdin.readline().rstrip()))
#
# straw_list.sort(reverse=True)
#
# i = 0
# found = -1
# while i <= len(straw_list)-3:
#     if straw_list[i] < straw_list[i+1] + straw_list[i+2]:
#         if found < straw_list[i] + straw_list[i+1] + straw_list[i+2]:
#             found = straw_list[i] + straw_list[i+1] + straw_list[i+2]
#     i += 1
#
# print(found)
# 1377 버블 소트
# 이건 버블소트로 구현을 한건데, 머지소트로 해야지 시간 초과가 안나기 때문에, 머지소트를 통해서
# 버블소트를 실행했을 때 버블소트가 실행 될 횟수를 구하는 문제

# 알고보니 파이썬 내장 정렬 함수가 팀정렬인데, 팀정렬은 머지소트를 최적화 시킨 정렬 방식으로
# 똑같이 stable sort이기 때문에 내장 정렬 함수를 사용해도 된다.
# 배열의 뒤에서 앞으로 간 값들 중에 가장 많이 옮겨진 값을 구하고, 옮겨진 만큼을 구하고,
# 1을 더하면 버블소트가 실행된 횟수를 구할 수가 있다.

# import sys
# num = int(sys.stdin.readline().rstrip())
# num_arr = []
# for i in range(num):
#     num_arr.append([int(sys.stdin.readline().rstrip()), i])
#
# num_arr.sort()
#
# ans = 0
#
# for i in range(num):
#     ans = max(ans, num_arr[i][1] - i + 1)
#
# print(ans)

# 11582 치킨 TOP N
# import sys
#
# num_size = int(sys.stdin.readline().rstrip())
#
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
# final = []
# people = int(sys.stdin.readline().rstrip())
#
# a = num_size // people
# i = 0
# while i <= num_size - a:
#     final.append(sorted(num_list[i:i+a]))
#     i += a
#
# for i in range(people):
#     for j in range(len(final[i])):
#         print(final[i][j], end = " ")

# ICPC 신촌 캠프 Lecture 3 출석 문제 및 연습 문제.

# 2504 괄호의 값
# import sys
#
# parent = list(sys.stdin.readline().rstrip())
# stack = []
# another_stack = []
# final_stack = []
# calc = -1
# for i in range(len(parent)):
#     if parent[i] == "(":
#         stack.append("(")
#         another_stack.append("2")
#         another_stack.append("(")
#     elif parent[i] == "[":
#         stack.append("[")
#         another_stack.append("3")
#         another_stack.append("(")
#     elif parent[i] == ")":
#         if len(stack) == 0 or stack.pop() != "(":
#             calc = 0
#             break
#         else:
#             if another_stack[-1] == "+":
#                 another_stack.pop()
#             another_stack.append(")")
#             if another_stack[-2] == "(":
#                 another_stack.pop()
#                 another_stack.pop()
#             another_stack.append("+")
#
#     elif parent[i] == "]":
#         if len(stack) == 0 or stack.pop() != "[":
#             calc = 0
#             break
#         else:
#             if another_stack[-1] == "+":
#                 another_stack.pop()
#             another_stack.append(")")
#             if another_stack[-2] == "(":
#                 another_stack.pop()
#                 another_stack.pop()
#             another_stack.append("+")
#     else:
#         calc = 0
#         break
# if len(stack) != 0:
#     calc = 0
#
#
# if calc == 0:
#     print(calc)
# else:
#     while another_stack[-1] == "+" or another_stack[-1] == "(":
#         another_stack.pop()
#
#     for i in another_stack:
#         if i == "(":
#             final_stack.append("*")
#         final_stack.append(i)
#
#     final = ''.join(final_stack)
#     calc = eval(final)
#     print(calc)
#
# 10828 스택
# import sys
#
# def push(string):
#     global stack, stack_size
#     a, b = string.split()
#     b = int(b)
#     stack.append(b)
#     stack_size += 1
#
# def pop():
#     global stack, stack_size
#     if stack_size != 0:
#         print(stack.pop(-1))
#         stack_size -= 1
#     else:
#         print(-1)
#
# def size():
#     global stack_size
#     print(stack_size)
#
# def empty():
#     global stack_size
#     if stack_size != 0:
#         print(0)
#     else:
#         print(1)
#
# def top():
#     global stack, stack_size
#     if stack_size != 0:
#         print(stack[-1])
#     else:
#         print("-1")
#
#
# oper_num = int(sys.stdin.readline().rstrip())
# stack = []
# stack_size = 0
# for i in range(oper_num):
#     operation = sys.stdin.readline().rstrip()
#     if operation[0:3] == "pus":
#         push(operation)
#     elif operation[0:3] == "pop":
#         pop()
#     elif operation[0:3] == "siz":
#         size()
#     elif operation[0:3] == "emp":
#         empty()
#     elif operation[0:3] == "top":
#         top()

# 18115 카드 놓기 한시간 반 뒤에 구글링
# import sys
# from collections import deque
# num = int(sys.stdin.readline().rstrip())
# card_list = deque()
#
# for i in range(1, num+1):
#     card_list.append(i)
#
# skill_list = list(map(int, sys.stdin.readline().rstrip().split()))
# skill_list = skill_list[::-1]
# final_list = deque()
#
# for i in skill_list:
#
#     if i == 1:
#         final_list.appendleft(card_list.popleft())
#     elif i == 2:
#         final_list.insert(1, card_list.popleft())
#     elif i == 3:
#         final_list.append(card_list.popleft())
#
# print(*final_list)

# 2304 창고 다각형
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# height_list = []
# stack = []
# for i in range(num):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     height_list.append([a, b])
#
# height_list.sort(key=lambda x: x[0])
# tallest_list = sorted(height_list, key=lambda  x: x[1], reverse=True)
# tallest = tallest_list[0][1]
# area = tallest
#
# start_index = height_list.index(tallest_list[0])
#
# i = start_index
# j = 0
# k = len(height_list) - 1
#
# a = 1
# while j < i:
#     if height_list[j][1] <= height_list[j+a][1]:
#         area += height_list[j][1] * (height_list[j+a][0] - height_list[j][0])
#         j += a
#         a = 1
#     else:
#         a += 1
# a = 1
# while k > i:
#     if height_list[k][1] <= height_list[k-a][1]:
#         area += height_list[k][1] * (height_list[k][0] - height_list[k-a][0])
#         k -= a
#         a = 1
#     else:
#         a += 1
#
# print(area)

#20923 숫자 할리갈리 게임
# import sys
# from collections import deque
# card_num, turn_num = map(int, sys.stdin.readline().rstrip().split())
# do_deck = deque()
# su_deck = deque()
# do_board = deque()
# su_board = deque()
# for i in range(card_num):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     do_deck.appendleft(a)
#     su_deck.appendleft(b)
#
# for i in range(turn_num):
#     if i % 2 == 0:
#         do_board.append(do_deck.popleft())
#     else:
#         su_board.append(su_deck.popleft())
#
#     if len(do_deck) == 0:
#         break
#     elif len(su_deck) == 0:
#         break
#
#     if (len(do_board) + len(su_board) > 1) and (do_board[-1] + su_board[-1] == 5):
#         if len(do_board) > 0:
#             su_deck += do_board
#         if len(su_board) > 0:
#             su_deck += su_board
#         do_board = deque()
#         su_board = deque()
#     elif (len(do_board) > 0 and do_board[-1] == 5) or (len(su_board) > 0 and su_board[-1] == 5):
#         if len(su_board) > 0:
#             do_deck += su_board
#         if len(do_board) > 0:
#             do_deck += do_board
#         do_board = deque()
#         su_board = deque()
#
# if len(do_deck) > len(su_deck):
#     print("do")
# elif len(do_deck) < len(su_deck):
#     print("su")
# else:
#     print("dosu")
#
#3078 좋은 친구 미해결
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().rstrip().split())
# deque_list = []
# for i in range(21):
#     deque_list.append(deque())
#
# count = 0
# for i in range(n):
#     name = sys.stdin.readline().rstrip()
#     if deque_list[len(name)]:
#         j = len(deque_list[len(name)]) - 1
#         while j >= 0:
#             if i - deque_list[len(name)][j] <= k:
#                 count += 1
#                 j -= 1
#             else:
#                 break
#     deque_list[len(name)].append(i)
#
# print(count)
#
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().rstrip().split())
# size_list = []
# count = 0
# for i in range(n):
#     size_list.append(len(sys.stdin.readline().rstrip()))
# queue = deque(size_list[:1+k])
# for i in range(1, len(queue)):
#     if queue[i] == queue[0]:
#         count += 1
#
# for i in range(1, n):
#     queue.popleft()
#     if i + k < n:
#         queue.append(size_list[i+k])
#     for i in range(1, len(queue)):
#         if queue[i] == queue[0]:
#             count += 1
#
# print(count)
#좋은 친구 해결 (이틀걸림)
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().rstrip().split())
# size_list = deque()
# for i in range(n):
#     size_list.append(len(sys.stdin.readline().rstrip()))
#
# each_count = [0] * 21
#
# queue = deque()
# count = 0
# while size_list:
#
#     temp1 = size_list.popleft()
#     queue.append(temp1)
#     each_count[temp1] += 1
#     if len(queue) > 1 + k:
#         temp2 = queue.popleft()
#         each_count[temp2] -= 1
#     if each_count[temp1] > 1:
#         count += (each_count[temp1] - 1)
#
# print(count)

#14889 스타트와 링크
#
# import sys
# from itertools import combinations, permutations
# num = int(sys.stdin.readline().rstrip())
# array = []
# temp = []
# for i in range(num):
#     array.append(list(map(int, sys.stdin.readline().rstrip().split())))
#     temp.append(i)
# list1 = list(combinations(temp, num//2))
# min_diff = 1000000000
# for i in list1:
#     alt_list = list(set(temp) - set(i))
#     list_temp = list(combinations(i, 2))
#     list_temp2 = list(combinations(alt_list, 2))
#     addition = 0
#     addition2 = 0
#     diff = 0
#     #print(i)
#     for j in list_temp:
#         #print(j)
#         addition += array[j[0]][j[1]] + array[j[1]][j[0]]
#     for j in list_temp2:
#         #print(j)
#         addition2 += array[j[0]][j[1]] + array[j[1]][j[0]]
#     diff = abs(addition - addition2)
#
#     #print(diff)
#     min_diff = min(diff, min_diff)
#
# print(min_diff)

#1182 부분수열의 합
#처음에 한 방법은 연속된 수열로 생각을 해서 틀렸다. 구글링을 통해 comb를 사용하면 된다는 걸
#찾았다
# import sys
# from itertools import combinations
# #a, b 값을 받는다
# a, b = map(int,sys.stdin.readline().rstrip().split())
# #숫자 배열을 받는다
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
# #숫자 배열을 정렬한다
# num_list.sort()
#
# #부분수열의 개수
# count = 0
#
# #combination을 통해서 각 길이의 경우의수들을 다 시도
# for i in range(1, a + 1):
#     comb = combinations(num_list, i)
#     for j in comb:
#         if sum(j) == b:
#             count += 1
#
# print(count)
