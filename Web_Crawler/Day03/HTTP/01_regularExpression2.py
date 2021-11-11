import re

msg1 = 'Johnson will attend my party tonight.'
msg2 = 'Johnnason will attend my party tonight.'
msg3 = 'Johnnananason will attend my party tonight.'

# search()返回string中第一個與pattern相匹配的字串,返回形式為Match物件，如果沒有匹配返回None
pattern = 'John((na)+son)'        # +:字串na可以1到多次
txt = re.search(pattern,msg1)
if txt != None:
    print(txt.group())
else:
    print(txt)                    # 因為沒有match所以不能使用group()


pattern = 'John((na)+son)'
txt = re.search(pattern,msg2)
print(txt.group())

pattern = 'John((na)+son)'
txt = re.search(pattern,msg3)
print(txt.group())

print("--------------------------------------------------")

pattern = 'John((na)*son)'             # *:字串na可以0到多次
txt = re.search(pattern,msg1)
print(txt.group())

pattern = 'John((na)*son)'
txt = re.search(pattern,msg2)
print(txt.group())

pattern = 'John((na)*son)'
txt = re.search(pattern,msg3)
print(txt.group())

print("--------------------------------------------------")

pattern = 'John((na)?son)'               # ?:字串na可以0或1次
txt = re.search(pattern,msg1)
print(txt.group())

pattern = 'John((na)?son)'
txt = re.search(pattern,msg2)
print(txt.group())

pattern = 'John((na)?son)'
txt = re.search(pattern,msg3)
print(txt)