import re

match=re.finditer("tca","TCAtcapradtca")
cnt=0

for data in match:
	print(f"{data.start()}--->{data.end()}--->{data.group()}")
	cnt=cnt+1
print(f"tca come {cnt} times")