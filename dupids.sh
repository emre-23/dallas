#print out the users with reded duplicated IDs

awk -F':' '{print $2}' data1.txt |sort|uniq -d|grep -F -f - user.txt

#second way
awk 'BEGIN { FS=":" } { c[$2]++; l[$2,c[$2]]=$0 } END { for (i in c) { if (c[i] > 1) for (j = 1; j <= c[i]; j++) print l[i,j] } }' user.txt





