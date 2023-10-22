import re

text = "hio 1238 dfasdlfk0kekw2 did you kn0w that v4pore0n"

print(re.findall("\d", text, re.IGNORECASE))
