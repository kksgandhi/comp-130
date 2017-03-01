import re

str ="This is a strangely spaced\tsample.\n\nIt is a string."
print(re.split(r"\s*",str))
print(re.split(r"\s+",str))
print(str.split())
