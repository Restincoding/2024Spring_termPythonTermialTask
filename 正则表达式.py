'''
一个利用了正则表达式的程序，能从给定文本中读取邮箱和号码
'''
import re

def regex(text="",default_text="小明的邮箱是2323232333@qq.com，电话是18907999999。"):
    
    if text=="":
        text=default_text
    else:
        text=text.strip()

    # 匹配邮箱地址
    email_pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    if emails:
        print("找到的邮箱地址：", "".join(emails))
    else:
        print("没有找到邮箱地址。")

    # 搜索电话号码
    phone_pattern=r"1\d{10}"
    phone_matches=re.findall(phone_pattern, text)
    if phone_matches:
        print("找到的电话号码：", "".join(phone_matches))
    else:
        print("没有找到电话号码。")

regex("这是什么我再想想")
regex("我的电话号码是 12345678901，邮箱是123456@gmail.com.")
regex()