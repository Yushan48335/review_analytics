data = []
count = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Total: ', len(data))