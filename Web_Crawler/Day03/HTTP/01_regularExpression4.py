import re

msg1 = 'Please call my secretary using 0937-000-123 or 0933-456-789'
msg2 = '請明天17:30和我一起參加成成獵才說明會'
msg3 = '請明天17:30和我一起參加成成獵才說明會, 可用0933-888-888聯絡我'

# findall會找到所以符合條件的內容
def parseString(string):

    pattern = r'\d{4}-\d{3}-\d{3}'
    # pattern = r'\d\d\d\d-\d\d\d-\d\d\d'    # 這種寫法也可以
    phoneNum = re.findall(pattern, string)   # findall()回傳的是以string組成的list
    print("電話號碼是: %s" % phoneNum)

parseString(msg1)
parseString(msg2)
parseString(msg3)

print("--------------------------------------------")

# search只會找到第一個符合條件的內容
def parseString(string):

    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string)    # search回傳的是re.Match的物件
    if phoneNum != None:
        print("電話號碼是: %s" % phoneNum.group())
    else:
        print("%s (字串不含電話號碼)" % string)

parseString(msg1)
parseString(msg2)
parseString(msg3)

print("--------------------------------------------")

def parseString(string):
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.findall(string)
    print("電話號碼是: %s" % phoneNum)

parseString(msg1)
parseString(msg2)
parseString(msg3)

print("--------------------------------------------")

def parseString(string):
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.search(string)
    if phoneNum != None:        # 檢查phoneNum內容
        print("電話號碼是: %s" % phoneNum.group())
    else:
        print("%s (字串不含電話號碼)" % string)

parseString(msg1)
parseString(msg2)
parseString(msg3)