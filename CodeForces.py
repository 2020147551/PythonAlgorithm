# Red Versus Blue
# Codeforces Round #782 (Div. 2) Problem A
# 2022-04-17

# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# for _ in range(num):
#     n, r, b = map(int, sys.stdin.readline().rstrip().split())
#     string = []
#
#     r_size = r//(b+1)
#     remaining = r%(b+1)
#
#     while len(string) < n:
#         for i in range(r_size):
#             string.append("R")
#         if remaining > 0:
#             string.append("R")
#             remaining -= 1
#         if len(string) < n:
#             string.append("B")
#
#     print(''.join(string))