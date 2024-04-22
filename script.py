import requests

# 指定要下载的文件的URL
url = 'https://images2.penguinrandomhouse.com/cover/tif/9780670786190'

# 指定下载到本地的文件路径
local_filename = 'download/tif'
if not os.path.exists(download):
        os.makedirs(download)

try:
    # 发送HTTP请求
    response = requests.get(url, stream=True)

    # 检查请求是否成功
    response.raise_for_status()

    # 以二进制写模式打开文件
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # 过滤掉保持连接的新的块
                f.write(chunk)
    print(f'文件已下载到 {local_filename}')
except requests.exceptions.HTTPError as err:
    print(f'下载过程中出现错误: {err}')
