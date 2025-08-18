import re
#dot meta character
pattarn = r"colo..r"

if re.match(pattarn, "colourr"):
    print("Matched")
