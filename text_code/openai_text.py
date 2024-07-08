from openai import OpenAI
client = OpenAI(
    base_url="http://36.129.32.46:26006/v1",
    api_key="abc123",
)

completion = client.chat.completions.create(
  model="qwen14b",
  messages=[
    {"role": "user", "content": "你叫什么名字？"}
  ]
)

print(completion.choices[0].message)