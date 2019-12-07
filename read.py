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

