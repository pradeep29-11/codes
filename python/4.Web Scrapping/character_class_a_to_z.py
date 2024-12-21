import re

matcher=re.finditer("[a]","tcaoradtaaa")

for match in matcher:
	print(f"{match.start()}--->{match.end()}--->{match.group()}")