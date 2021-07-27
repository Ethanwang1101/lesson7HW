score = []
x = int (input('學生數量'))

for i in range(x):
    y = str (input('學生名字'))
    z = int (input('學生成績'))
    score.append(z)

max_num = max(score)
print(max_num)
min_num = min(score)
print(min_num)
sum_num = sum(score)
print(sum_num)
sum_num = sum(score)/x
print(sum_num)