import re

text = "The ghost that says boo haunts the loo."

print(re.findall(".oo", text, re.IGNORECASE))
