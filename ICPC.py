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