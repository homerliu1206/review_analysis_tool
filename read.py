data = []
count = 0

with open ('reviews.txt','r') as f:  
	for line in f:
		data.append (line)
		count +=1
		if count % 1000 == 0:  #每一千筆print一次
			print (len(data))

print ('檔案讀取完畢，共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  #sum_lem += len(d)

print ('每則留言平均長度為', sum_len / len(data))

