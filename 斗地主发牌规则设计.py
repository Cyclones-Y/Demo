# 重新导入必要的库
# import random
# import pandas as pd
# from memory_profiler import memory_usage
#
# # 重新定义数据和函数
# data = {
#     'ID': list(range(1, 55)),
#     'Value': [
#         103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406,
#         107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410,
#         111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413, 114, 115, 101, 201,
#         301, 401, 102, 202, 302, 402
#     ]
# }
# df = pd.DataFrame(data)
#
# def simulate_cut_and_shuffle(deck_df, num_shuffles=10):
#     for _ in range(num_shuffles):
#         cut_point = random.randint(0, len(deck_df) - 1)
#         top = deck_df.iloc[:cut_point]
#         bottom = deck_df.iloc[cut_point:]
#         deck_df = bottom.append(top, ignore_index=True)
#         # for _ in range(random.randint(1, 10)):
#         #     idx1, idx2 = random.sample(range(len(deck_df)), 2)
#         #     deck_df.iloc[idx1], deck_df.iloc[idx2] = deck_df.iloc[idx2], deck_df.iloc[idx1]
#     return deck_df
#
#
# simulate = simulate_cut_and_shuffle(df, num_shuffles=10)
# print(simulate[:17])


import random
import pandas as pd

# 重新定义数据和函数
data = {
    'ID': list(range(1, 55)),
    'Value':
        [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
         6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
         9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11,
         12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14,
         14, 15, 15, 15, 15, '小王', '大王']
}
df = pd.DataFrame(data)


def simulate_cut_and_shuffle(deck_df, num_shuffles=5):
    for _ in range(num_shuffles):
        cut_point = random.randint(0, len(deck_df) - 1)
        top = deck_df.iloc[:cut_point]
        bottom = deck_df.iloc[cut_point:]
        deck_df = bottom.append(top)
    return deck_df


simulate = simulate_cut_and_shuffle(df, num_shuffles=5)
print(simulate[:17])
print(simulate[17:34])
print(simulate[34:51])
print(simulate[51:])

# # 定义一个监控函数来记录内存使用情况
# def memory_usage_simulate_shuffling():
#     # 运行洗牌函数
#     shuffled_deck = simulate_cut_and_shuffle(df, num_shuffles=10)
#     # 获取前17张牌的数据
#     return shuffled_deck.head(17)
#
# # 测量内存使用情况
# mem_usage = memory_usage(memory_usage_simulate_shuffling)  # memory_usage函数调用监控函数并返回内存使用列表
#
# # 输出内存使用情况
# mem_usage, max(mem_usage) - min(mem_usage)
