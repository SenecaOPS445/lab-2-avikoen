#!/usr/bin/env python3
# Author: Avi Koen
# Author ID: YourSenecaID
# Date Created: 2024/05/24

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')

