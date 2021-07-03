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

#그리디 알고리즘 기출문제 1번 모험가 길드
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

#그리디 알고리즘 기출문제 2번 곱하기 혹은 더하기
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

#그리디 알고리즘 기출문제 3번 문자열 뒤집기

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
# 백준 1541번 미해결
import sys

working_list = sys.stdin.readline().rstrip()

if "-" not in working_list:
    print(eval(working_list))
elif "+" not in working_list:
    print(eval(working_list))
else:
    list(working_list)
    index_of_add = [int(i) for i, x in enumerate(working_list) if x == "+"]
    index_of_sub = [int(i) for i, x in enumerate(working_list) if x == "-"]
    index_of_all = index_of_sub + index_of_add
    index_of_all.sort()
    index_of_num = []
    inverted_num = []
    i = 0
    temp = 0
    while i <= len(working_list):
        if i == len(working_list):
            index_of_num.append([int(temp), int(i)])
            break
        elif i not in index_of_add and i not in index_of_sub:
            i += 1
        else:
            index_of_num.append([int(temp), int(i)])
            i += 1
            temp = i

    for i in range(len(index_of_sub)-1):
        inverted_num.append(int(eval(str(working_list[index_of_sub[i]+1:index_of_sub[i+1]]))))


    if index_of_sub[len(index_of_sub)-1] == index_of_all[len(index_of_all)-1]:
        inverted_num.append(int(working_list[index_of_sub[len(index_of_sub)-1]+1:]))
        working_list.replace(working_list[index_of_sub[len(index_of_sub)-1]+1:], "")
    else:
        inverted_num.append(int(working_list[index_of_sub[len(index_of_sub) - 1]:index_of_all[len(index_of_all) - 1]]))
        working_list.replace(working_list[index_of_sub[len(index_of_sub) - 1]:index_of_all[len(index_of_all) - 1]], "")

print(working_list)
print(inverted_num)
print(index_of_sub)
print(index_of_all)
