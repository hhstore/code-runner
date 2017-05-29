#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random


# 生成随机ID
def create_uuid():
    ts = int(time.time() * 1000) - 1400000000000
    value = (ts << 16) + random.randint(0, 65535)
    return hex(value)[2:-1]
