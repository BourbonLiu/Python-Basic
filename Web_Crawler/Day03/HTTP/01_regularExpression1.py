import re
msg = 'cat hat sat at matter flat hot'

# findall()返回string中所有與pattern相匹配的全部字串,返回形式為list
pattern = '.at'                          # .:任一字元
txt = re.findall(pattern,msg)
print(txt)

pattern = "^c"                           # ^:比對整個字串的開始，以c開頭
txt = re.findall(pattern,msg)
print(txt)

pattern = "..t$"                         # $:比對整個字串的結尾，以t結尾
txt = re.findall(pattern,msg)
print(txt)

pattern = "^c|.at"                       # 以c開頭或.at的字串
txt = re.findall(pattern,msg)
print(txt)

print("----------------------------------------------------------")

# match()從首字母開始開始匹配,string如果包含pattern子串,則匹配成功,返回Match物件,失敗則返回None。
pattern = "^c.*t$"
txt = re.match(pattern,msg)
print(txt)
print(txt.group())                       # group()會把Match物件裡的所有東西變成一個string

