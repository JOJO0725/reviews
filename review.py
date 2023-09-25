data = []
count = 0
new = []
with open('reviews.txt','r') as r:
    for line in r:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
print('檔案讀取完畢!共',len(data),'比留言!')
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
    avg = sum_len / len(data)
    if len(d) < 100:
        new.append(d)
print('少於100字的留言共',len(new),'筆')
print('留言平均的長度:',avg)




