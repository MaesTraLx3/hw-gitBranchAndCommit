# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333

import sys
import requests
import re
from bs4 import BeautifulSoup

username = ''

def hw1():
    response = requests.get('ttps://raw.githubusercontent.com/{}/hw-gitBranchAndCommit/theLooooooooooongestBranch/1plus1.txt')
    sys.exit(0 if '1+1=2' in response.text.strip().replace(' ', '') else -1)

methods = [hw1]
if __name__ == '__main__':
    hw_index = re.findall(r'I finished homework: `1`', sys.argv[1])[0]
    username = re.findall(r'`https://github.com/(.*?)/hw-gitBranchAndCommit`', sys.argv[1])[0]
    methods[hw_index - 1]()