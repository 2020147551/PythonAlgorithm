# 백준 1541번 미해결
# import sys
#
# working_list = sys.stdin.readline().rstrip()
#
# if "-" not in working_list:
#     print(eval(working_list))
# elif "+" not in working_list:
#     print(eval(working_list))
# else:
#     list(working_list)
#     index_of_add = [int(i) for i, x in enumerate(working_list) if x == "+"]
#     index_of_sub = [int(i) for i, x in enumerate(working_list) if x == "-"]
#     index_of_all = index_of_sub + index_of_add
#     index_of_all.sort()
#     index_of_num = []
#     inverted_num = []
#     i = 0
#     temp = 0
#     while i <= len(working_list):
#         if i == len(working_list):
#             index_of_num.append([int(temp), int(i)])
#             break
#         elif i not in index_of_add and i not in index_of_sub:
#             i += 1
#         else:
#             index_of_num.append([int(temp), int(i)])
#             i += 1
#             temp = i
#
#     for i in range(len(index_of_sub)-1):
#         inverted_num.append(int(eval(str(working_list[index_of_sub[i]+1:index_of_sub[i+1]]))))
#
#
#     if index_of_sub[len(index_of_sub)-1] == index_of_all[len(index_of_all)-1]:
#         inverted_num.append(int(working_list[index_of_sub[len(index_of_sub)-1]+1:]))
#         working_list.replace(working_list[index_of_sub[len(index_of_sub)-1]+1:], "")
#     else:
#         inverted_num.append(int(working_list[index_of_sub[len(index_of_sub) - 1]:index_of_all[len(index_of_all) - 1]]))
#         working_list.replace(working_list[index_of_sub[len(index_of_sub) - 1]:index_of_all[len(index_of_all) - 1]], "")
#
# print(working_list)
# print(inverted_num)
# print(index_of_sub)
# print(index_of_all)

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
