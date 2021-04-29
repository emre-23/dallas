from collections import defaultdict

res = defaultdict(list)

with open('data1.txt') as infile:
    for line in infile:
        val = line.strip().split()
        res[val[0]].append(line)

for k, v in res.items():
    if len(v) > 1:
        print(v)
