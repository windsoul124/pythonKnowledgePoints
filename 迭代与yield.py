# #  for循环的迭代器协议
# class something:
#     def __init__(self):
#         pass
#     def __iter__(self):
#         pass
# for x in something:
#     print(x)
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num +=1
    return nums

sum_of  = sum(firstn(100000000000000000000000000000000))