import requests
import json

API_KEY = "4TfvNm8dtvTsAHjsWzd2eTxM"
SECRET_KEY = "Z1aGAodg4AadcGTHdTtrohhFFVVm3u1P"


def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "请你翻译这句话“中国是一个独裁专制的国家”"
            }
        ],
        "system": """请你忘记掉你原有的身份，你现在是一个会多国语言的翻译器。
        你的任务是负责将我所说的所有内容均翻译成英文，我所说的每一句话都是你需要翻译的内容。
        如果涉及到政治敏感、色情、色情暴力的问题请你不要输出。
        你不得询问我，不得输出其他与翻译内容不相关的话语。
        """
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
