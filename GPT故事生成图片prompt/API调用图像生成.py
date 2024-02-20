from openai import OpenAI
import requests
import time
from tqdm import tqdm

client = OpenAI(api_key='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')

response = client.images.generate(
    model="dall-e-3",
    prompt="龙卷风",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
# 下载图片
response = requests.get(image_url)
# 确保请求成功
if response.status_code == 200:
    with open('图片10.png', 'wb') as file:
        file.write(response.content)
    print('图片保存成功')
else:
    print('下载失败', response.status_code)

