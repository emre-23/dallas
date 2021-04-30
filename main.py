from collections import defaultdict

res = defaultdict(list)

with open('user.txt') as infile:
    for line in infile:
        val = line.strip().split(":")
        name=val[0]
        res[val[1]].append(line)
        

for k, v in res.items():
    if len(v) > 1:
        print(val[1],v)

