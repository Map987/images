
import os
import requests


# 文件下载地址
url = 'https://images2.penguinrandomhouse.com/cover/tif/9780670786190'

# 目标文件夹
folder = 'download'

# 确保文件夹存在
if not os.path.exists(folder):
    os.makedirs(folder)

# 文件名（从URL中提取）
filename = url.split('/')[-1]

# 完整的文件路径
file_path = os.path.join(folder, filename)

# 下载文件
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 检查请求是否成功

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"文件已下载: {file_path}")
except requests.exceptions.HTTPError as err:
    print(f"下载过程中发生错误: {err}")
