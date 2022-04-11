data = []
count = 0
with open('reviews.txt', 'r') as R:
	for line in R :
		data.append(line)
		count += 1
		if count % 1000 == 0:
		 	print(len(data))
print(len(data))	
print(data[0])
