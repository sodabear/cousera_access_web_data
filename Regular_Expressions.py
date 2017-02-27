import re
import sys

fname = "regex_sum_332355.txt"
with open(fname) as f:
	content = f.read()

# r'\d+’ 等于r'[0,9]+'
ans = re.findall(r'[0-9]+', content)
ans = [int(i) for i in ans]
print(ans)
print(sum(ans))


