import random

def weighted_choice(values, probabilities):
    """
    根据给定的概率从值列表中选择一个值

    参数:
    values (list): 值列表
    probabilities (list): 对应值的概率列表

    返回:
    选择的值
    """
    # 使用random.choices方法，根据概率选择一个值
    return random.choices(values, probabilities)[0]

# 示例值和概率
values = ['A', 'B', 'C', 'D']
probabilities = [0.1, 0.2, 0.3, 0.1]

# 调用函数并打印结果
result = weighted_choice(values, probabilities)
print("选择的值:", result)