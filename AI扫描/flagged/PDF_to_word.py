import io

import requests
import base64
import urllib
import gradio as gr

API_KEY = "pSm"
SECRET_KEY = "XUe"


# 获取PDF task_id
def pdf2task_id():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_convert/request?access_token=" + get_access_token()

    # 获取文件的64位编码
    pdf_base64 = get_file_content_as_base64('AI翻译提示词.pdf', True)
    payload = 'pdf_file=' + pdf_base64

    # 返回任务信息
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # result_data = response.json().get('result', {}).get('result_data')
    # pdf_b64 = result_data.json()
    print(response)
    # return pdf_b64['result']['result_data']


# 通过task_id生成word文档下载链接
def pdf_to_word():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_convert/get_request_result?access_token=" + get_access_token()

    payload = pdf2task_id
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    file2word = response.json()
    print(file2word)


# 文件编码函数
def get_file_content_as_base64(path, urlencoded=False):
    # buffered = io.BytesIO()
    # file.save(buffered, format='PDF')
    # content = base64.b64decode(buffered.getvalue()).decode('utf-8')
    # if urlencoded:
    #     content = urllib.parse.quote_plus(content)
    # return content
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__pdf_to_word__':
    pdf_to_word()

# # 创建Gradio界面
# iface = gr.Interface(
#     fn=pdf_to_word,
#     inputs=gr.File(type='filepath',label="上传PDF文件"),
#     outputs=gr.Text(label='Word文件下载链接'),
#     title='PDF 转 Word',
#     description="上传一个 PDF 文件，获取转换后的 Word 文件下载链接。"
# )
#
# iface.launch()
