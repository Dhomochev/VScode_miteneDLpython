#   2025/09/21   v0_0
# - module install : requests, beautifulsoup4
# - 参考）https://blog.takuya-andou.com/entry/2023/08/07/085328
#  https://mitene.us/f/bNHVoBH_BzI　　　(pw:*)
#  mitene-DL-v0_0.py

import os
import requests
import json
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime

dl_dir = 'dl'
os.makedirs(dl_dir, exist_ok=True)

def save_files(url, page):
    if page%10==0:
        print(page)
    req_url = url+f"?page={page}"
    response = requests.get(req_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # JavaScript変数gonを取得
    script = soup.find("script").string

    # "gon.media"から";"までを抽出
    match = re.search(r'gon.media=(.*?);', script)
    if match:
        json_string = match.group(1)
        # 最後の"}"以降を削除
        json_string = json_string.rsplit("}", 1)[0] + "}"
        gon = json.loads(json_string)
    else:
        raise Exception("Could not find JavaScript variable 'gon'")

    # メディアファイルを保存
    for media_file in gon["mediaFiles"]:
        took_at = media_file["tookAt"]
        took_at_datetime = datetime.fromisoformat(took_at.replace("Z", "+00:00"))
        took_at_str = took_at_datetime.strftime("%Y%m%d%H%M%S")
        filename = f'{took_at_str}.{media_file["contentType"].split("/")[-1]}'
        
        file_path = os.path.join(dl_dir, filename)
        media_url = f'{url}/media_files/{media_file["uuid"]}/download'
        response = requests.get(media_url)  # メディアファイルのURLを取得
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        # 負荷をかけないように1秒につき１枚
        time.sleep(1)

    # 次のページが存在する場合は再帰的に処理
    if gon["hasNext"]:
        save_files(url, page+1)


if __name__ == "__main__":
    url = "https://mitene.us/f/bNHVoBH_BzI"  # アルバムのURL
    print(url)
    save_files(url, 1)  # 初回の呼び出し






