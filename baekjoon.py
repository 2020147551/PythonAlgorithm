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
