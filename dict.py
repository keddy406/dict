data = []

with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #加一
		else: 
			wc[word] = 1 #新增進去
for word in wc:
	if wc[word] >= 100000:
		
		print(word,wc[word])

while True:
	word = input('你想查找什麼字:')
	if word == 'q':
		break
	elif word in wc:
		print(word,'字典中出現' , wc[word] , '次')
	else:
		print('沒有出現過哦')
print('thanks for seraching')