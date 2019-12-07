data = []
count = 0
total_len = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
		total_len += len(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
ave_len = total_len / len(data)
print('Total: ', len(data), ', average for every line is: ', ave_len)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆留言長度小於100')
print('第一筆留言：', new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '提到good')
print('第一筆有提到good的留言如下：', good[0])

