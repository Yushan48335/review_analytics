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

