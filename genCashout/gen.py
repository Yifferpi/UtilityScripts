#! /usr/bin/env python3

import re

project = "./"
in_file = "{}data.txt".format(project)

with open(in_file) as f:
    content = f.read()
    keys = re.findall(r"%(.+):", content)
    print(keys)
    values = re.findall(r":\s*([\w\W]+?)\s*(?:%|$)", content)
    print(values)

options = zip(keys, values)
for p in options:
    print(p)

