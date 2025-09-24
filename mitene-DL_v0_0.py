#   2025/09/21   v0_0
# - module install : requests, beautifulsoup4
#
#  https://mitene.us/f/QkjREtbKY5M
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






if __name__ == "__main__":
    url = "https://mitene.us/f/QkjREtbKY5M"  # アルバムのURL
    save_files(url, 1)  # 初回の呼び出し






