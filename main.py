import sys

#그리디 알고리즘 1번 큰수의 법칙
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

#그리디 알고리즘 2번 숫자 카드 게임
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
# num_list = list()
# for i in range(a):
#     num_list.append(min(list(map(int, sys.stdin.readline().rstrip().split()))))
#
# print(max(num_list))

#그리디 알고리즘 3번 1이 될 때까지
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
