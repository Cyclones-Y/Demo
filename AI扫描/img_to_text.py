import io
import gradio as gr
import base64
import urllib
import requests
import json

image_word_API_KEY = "pS3lR7H24aWefWhyt4MZ4yHm"
image_word_SECRET_KEY = "Xc9dHDUg4EiENWDEK9U6GcAlxrZX11De"
wenxin_API_KEY = "vxQOoOXPpMIM66yaaGhDd69Y"
wenxin_SECRET_KEY = "Nbt4lY5KCMaDp0F3oe8wsEt2Gketx8rP"


def main(image):
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis?access_token=" + OCR_get_access_token()
    # image 可以通过 get_file_content_as_base64("C:\fakepath\测试题.jpg",True) 方法获取
    image_base64 = get_file_content_as_base64(image, True)
    payload = 'image=' + image_base64 + ('&detect_direction=true&line_probability=false&disp_line_poly=false'
                                         '&words_type=handwring_only&layout_analysis=false&recg_formula=true')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    word2txt = response.json()
    wordlist = []
    for item in word2txt["results"]:
        wordlist += item["words"]['word']
    complete_sentence = ' '.join(wordlist)
    return complete_sentence

    # print(response.text)


def get_file_content_as_base64(image, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    # with open(path, "rb") as f:
    #     content = base64.b64encode(f.read()).decode("utf8")
    #     if urlencoded:
    #         content = urllib.parse.quote_plus(content)
    # return content
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    content = base64.b64encode(buffered.getvalue()).decode("utf8")
    if urlencoded:
        content = urllib.parse.quote_plus(content)
    return content


def wenxin_main(user_input):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + wenxin_get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    wenxin_response = response.json()
    # 返回 API 的响应结果
    return wenxin_response.get("result", "未能获取响应")


def OCR_get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": image_word_API_KEY,
              "client_secret": image_word_SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def wenxin_get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": wenxin_API_KEY, "client_secret": wenxin_SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# 创建 Gradio 界面

def process_input(choice, image, text):
    if choice == "图片转文字":
        if image is None:
            return "请上传图片。"
        return main(image)  # 调用图片处理函数
    elif choice == "文本对话":
        if text.strip() == "":
            return "请输入文本。"
        return wenxin_main(text)  # 调用文本处理函数
    else:
        return "请选择操作类型。"


# 创建 Gradio 界面
iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Dropdown(label="选择操作", choices=["图片转文字", "文本对话"]),
        gr.Image(type="pil", label="上传图片"),
        gr.Textbox(label="输入文本")
    ],
    outputs="text",
    title="图片转文字与对话功能",
    description="选择操作类型并输入相应内容。"
)
# 启动应用
iface.launch(share=True)
#
# # 图片转文字的标签页
# with gr.Blocks() as demo:
#     with gr.Tab("图片转文字"):
#         with gr.Row():
#             image_input = gr.Image(type="pil")
#             image_output = gr.Text()
#         image_input.change(fn=main, inputs=image_input, outputs=image_output)
#
#     with gr.Tab("文字对话"):
#         with gr.Row():
#             text_input = gr.Textbox()
#             text_output = gr.Text()
#         text_input.change(fn=wenxin_main, inputs=text_input, outputs=text_output)
# # 启动应用
# demo.launch(share=True)
