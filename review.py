data = []
count = 0
new = []
goods = []
with open('reviews.txt','r') as r:
    for line in r:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
# print('檔案讀取完畢!共',len(data),'比留言!')
# print(data[0])
wc = {}
count = 1
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
print(len(wc))
print(wc['Allen'])
while True:
    key_word = input('請輸入關鍵字:(q:離開)')
    if key_word == 'q':
        break
    elif key_word not in wc:
        print('字典中沒有這個字!')    
    else:
        count = wc[key_word]
        print(key_word, '出現的次數出現', count, '次!')




















# sum_len = 0
# for d in data:
#     sum_len = sum_len + len(d)
#     avg = sum_len / len(data)
#     if len(d) < 100:
#         new.append(d)
# print('少於100字的留言共',len(new),'筆')
# print('留言平均的長度:',avg)

# for good in data:
#     if 'good' in good:    
#         goods.append(good)

# print('有提到 good 得流言有',len(goods),'筆!')

# # 
