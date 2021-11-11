import re

msg1 = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
msg2 = "1. cat, 2. dogs, 3. pigs, 4. swans"

pattern = '[aeiouAEIOU]'
txt = re.findall(pattern,msg1)      # 搜尋有[aeiouAEIOU]字元
print(txt)

pattern = '[2-5].'                  # 搜尋有[2-5.]字元
txt = re.findall(pattern,msg2)
print(txt)

print("-------------------------------------------------------")

pattern = '[^aeiouAEIOU]'
txt = re.findall(pattern,msg1)       # 搜尋沒有[aeiouAEIOU]字元
print(txt)

pattern = '[^2-5.]'                  # 搜尋沒有[2-5.]的字元
txt = re.findall(pattern,msg2)
print(txt)

print("-------------------------------------------------------")

pattern = '\w+'                      # w:文字
txt = re.findall(pattern,msg1)
print(txt)

pattern = 'John\w*'
txt = re.findall(pattern,msg1)
print(txt)

pattern = '\d+\D\s\w+'                # d:數字 s:空白 w:文字
txt = re.findall(pattern,msg2)
print(txt)

# \d 0-9整數                \D 0-9整數以外的字元
# \s 空白、換行              \S 空白、換行以外的字元
# \w 數字、大小寫子母、底線    \W 數字、大小寫子母、底線以外的字元
