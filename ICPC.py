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

#ICPC 신촌 캠프 Lecture 2 출석 문제 및 연습 문제

#10825 국영수
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
#10610 30
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

#2437 저울
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

#1448 삼각형 만들기
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
#1377 버블 소트
#이건 버블소트로 구현을 한건데, 머지소트로 해야지 시간 초과가 안나기 때문에, 머지소트를 통해서
#버블소트를 실행했을 때 버블소트가 실행 될 횟수를 구하는 문제
import sys
num = int(sys.stdin.readline().rstrip())
num_arr = []
for i in range(num):
    num_arr.append(int(sys.stdin.readline().rstrip()))

change = False

i = 1
while i <= num+1:
    change = False
    j = 0
    while j < num-i:
        if num_arr[j] > num_arr[j+1]:
            change = True
            num_arr[j], num_arr[j+1] = num_arr[j+1], num_arr[j]
        j += 1
    if change == False:
        print(i)
        break
    i += 1



