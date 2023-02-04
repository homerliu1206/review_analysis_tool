data = []
count = 0

# 讀取檔案
with open ('reviews.txt','r') as f:  
	for line in f:
		data.append (line)
		count +=1
		if count % 1000 == 0:  #每一千筆print一次
			print (len(data))
print ('檔案讀取完畢，共有', len(data), '筆資料')

# 計算留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #sum_lem += len(d)
print ('每則留言平均長度為', sum_len / len(data))

# 計算字數小於100
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '則留言長度小於100')

# 計算幾筆留言包含good
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print ('共有', len(good), '筆留言提到「good」')


# 計算字頻
wc = {}  # word_count
for d in data:
	words = d.split()  # 預設即為空白健，且可判別連續空格
	for word in words: 
		if word in wc:
			wc[word] += 1  # 曾經出現時，則value + 1
		else:
			wc[word] = 1  # 未曾出現時，宣告value為1

for word in wc:
	if wc[word] > 10000:
		print (word, wc[word])  # 前key後value，使資料分行


# 計算總字數
print (len(wc))

# 查詢字詞
while True:
	word = input ('請問您想查詢的字詞:')
	if word == 'q':
		print ('感謝使用本查詢功能')
		break
	if word in wc:
		print (word, '出現過的次數為', wc[word])
	else:
		print ('查無此字')
