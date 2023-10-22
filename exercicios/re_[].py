import re

text = "Two too"

print(re.findall("t[ow]o", text, re.IGNORECASE))
