import os

import requests


def download_file(url, save_directory, filename=None):
    try:
        # 发送HTTP请求获取文件内容
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，则抛出HTTPError异常

        # 确定文件名
        if not filename:
            filename = os.path.basename(url)

        # 创建保存目录（如果不存在）
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # 构建本地文件路径
        local_path = os.path.join(save_directory, filename)

        # 将文件内容写入本地文件
        with open(local_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded and saved to: {local_path}")
        return local_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None

if __name__ == "__main__":
    # 示例调用
    url = "https://netbid-new.lnwlzb.com/unzip/pdf/upzip/2024-06-05/09b33f63-95d1-4c67-9d6f-81e8420d5c2e/投标正文/1.2投标函附录.pdf"
    save_directory = "/mnt/d/Review"
    downloaded_file_path = download_file(url, save_directory)
    print(f"Downloaded file path: {downloaded_file_path}")