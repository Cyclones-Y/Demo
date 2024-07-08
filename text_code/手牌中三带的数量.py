# 假设你的手牌是一个列表
hand = ["3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2", "小王", "大王"]

# 创建一个字典来存储每张牌的出现次数
card_count = {}

# 遍历手牌，将每张牌的出现次数记录在字典中
for card in hand:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

# 统计出现次数为三的牌的数量
three_of_a_kind_count = 0
for count in card_count.values():
    if count == 3:
        three_of_a_kind_count += 1

# 打印结果
print("手牌中有三个相同牌的数量:", three_of_a_kind_count)

