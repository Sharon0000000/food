data = []
with open('food.txt', 'r') as f:
	for a in f:
		data.append(a.strip())

print(data)