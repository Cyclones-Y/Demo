import random
import pandas as pd

# 定义数据
data = {
    'ID': list(range(1, 55)),
    'Value':
        [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
         6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
         9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11,
         12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14,
         14, 15, 15, 15, 15, 16, 17]
}

# 创建DataFrame
df = pd.DataFrame(data)


# 定义模拟切牌和洗牌的函数
def simulate_cut_and_shuffle(deck_df, num_shuffles=5):
    for _ in range(num_shuffles):
        cut_point = random.randint(0, len(deck_df) - 1)
        top = deck_df.iloc[:cut_point]
        bottom = deck_df.iloc[cut_point:]
        deck_df = pd.concat([bottom, top], ignore_index=True)
    return deck_df


# 生成500份数据
shuffled_data = [simulate_cut_and_shuffle(df, num_shuffles=5) for _ in range(500)]

# # 创建一个大的DataFrame来保存所有洗牌的结果
# big_df = pd.DataFrame()
#
# for single_shuffle in shuffled_data:
#     # 分配牌给三位玩家
#     player_cards = [single_shuffle.iloc[i * 17:(i + 1) * 17, 1].tolist() for i in range(3)]
#     # 转换每位玩家的手牌为字符串，并计算手牌的种类数量
#     for cards in player_cards:
#         cards_str = ','.join(map(str, cards))
#         card_count = len(set(cards))
#         big_df = big_df.append({'玩家手牌': cards_str, '玩家手牌数': card_count}, ignore_index=True)
#
# # 保存到CSV文件
# csv_file_path = 'shuffled_decks_processed.csv'
# big_df.to_csv(csv_file_path, index=False, header=True)
#
# print(f"Data saved to {csv_file_path}")

# 创建一个大的DataFrame来保存所有洗牌的结果
all_data = []

for single_shuffle in shuffled_data:
    # 分配牌给三位玩家
    player_cards = [single_shuffle.iloc[i * 17:(i + 1) * 17, 1].tolist() for i in range(3)]
    # 每位玩家的手牌和手牌种类数量
    row_data = []
    for cards in player_cards:
        cards_str = ','.join(map(str, cards))
        card_count = len(set(cards))
        row_data.extend([cards_str, card_count])
    all_data.append(row_data)

# 将所有洗牌结果转换为DataFrame
column_names = ['玩家0手牌', '玩家0手牌数', '玩家1手牌', '玩家1手牌数', '玩家2手牌', '玩家2手牌数']
processed_df = pd.DataFrame(all_data, columns=column_names)

# 保存到CSV文件
csv_file_path = 'shuffled_decks_processed.csv'
processed_df.to_csv(csv_file_path, index=False, header=True)

print(f"Data saved to {csv_file_path}")
