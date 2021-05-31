import pandas as pd
df = pd.read_excel("Книга1.xlsx")

for i, item in df['TestResultB'].items():
    target = []
    for x in str(item):      
        if x == '+':
            target.append(1)
        elif x == '-':
            target.append(0)
        else:
            target.append(x)
    aa = ''.join(map(str, target))
    df['TestResultB'][i] = aa
    target = []

for i, item in df['TestResultC'].items():
    if item != item:
        df['TestResultC'][i] = item
    else:
        a = item[0::4]
        df['TestResultC'][i] = a


for i, item in df['TestResultD'].items():
    if item != item:
        df['TestResultD'][i] = item
    else:
        l = item[0::4]
        df['TestResultD'][i] = l

print(df['TestResultD'])

df.to_excel('alldata2020.xlsx')

