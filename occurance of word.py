visited = []
f = open("text.txt","r")
s = f.read().split()
for each in s:
	if each not in visited:
		print(each, "  ", s.count(each))
		visited.append(each)
f.close()