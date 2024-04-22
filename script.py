import requests
import os

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

# 使用环境变量来设置URL和本地文件名
url = os.getenv('DOWNLOAD_URL')
local_filename = os.getenv('LOCAL_FILENAME')

if url and local_filename:
    download_file(url, local_filename)
    print(f"File downloaded: {local_filename}")
else:
    print("Environment variables not set.")
