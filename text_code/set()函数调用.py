# nums_list = [2,2,1,1,1,2,2,2,1,1,1,2]
# nums_list.sort()
# num = len(nums_list) // 2
# a = nums_list[num]
# print(a)

#
# nums = [3,3,4]
# def majorityElement(nums) -> int:
#     num_dict = {}
#     for i in nums:
#         if i in num_dict:
#             num_dict[i] += 1
#         else:
#             num_dict[i] = 1
#     print(max([i for i in num_dict if num_dict[i] > len(nums)//2]))
#     return max([i for i in num_dict if num_dict[i] > len(nums)//2])
#
def climbStairs(n: int) -> int:
    # dp[i] 为第 i 阶楼梯有多少种方法爬到楼顶
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climbStairs(4))
