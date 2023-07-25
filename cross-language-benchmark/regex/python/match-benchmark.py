#!/usr/bin/env python3

import subprocess
import re



pattern = re.compile("s\\w+g")
for i in range(100_000_000):
	re.search(pattern, "some-string-for-match")
