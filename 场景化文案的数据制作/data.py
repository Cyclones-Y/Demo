# -*- coding: utf-8 -*-

from openai import OpenAI

client = OpenAI(api_key='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')

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "system",
            # "content": ''
            "content": "请你写一段场景化文案，即能给用户制造一个场景想象或场景联想，通过在相同或类似的场景下触景生情而联想到产品\n\n请你根据以下示例仿写一段：“\n1.卖大米\n我没有带你去看过长白山皑皑的白雪，我没有带你去感受过十月田间吹过的微风，我没有带你去看过沉甸甸地弯下腰，犹如智者一般的谷穗，我没有带你去见证过这一切，但是，亲爱的，我可以让你品尝这样的大米。\n\n2.卖玉米\n好多年后你回忆起来，其实那个玉米的味道记不太清楚了，尝着好像很香。但你清楚记得的是，那些仲夏的夜里，繁星点缀，树叶沙沙作响，那时候你头也不疼，颈椎也不疼，也不会在失眠的夜里头辗转反侧，也不会在睡醒的早晨头昏脑胀，那时候你爸妈身体还很健康，他们年轻，平安喜乐，爷爷奶奶也陪在你身边。你其实不是想玉米，你是想当年的自己啊……”"
        }

        # {
        #     "role": "user",
        #     "content": "你叫什么名字"
        # }
    ],
    temperature=1,
    max_tokens=2024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stream=True
)
full_response = ""
for i in response:
    content = i.choices[0].delta.content
    if content is not None:
        full_response += content

print(full_response)
