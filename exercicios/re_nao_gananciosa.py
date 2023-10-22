import re

text = "_hi__bye__cry_ sore ga mo toki"

print(re.findall("_.*_", text, re.IGNORECASE))
print(re.findall("_.*?_", text, re.IGNORECASE))
