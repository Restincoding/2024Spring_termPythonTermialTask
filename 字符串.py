'''
编写了一个字符串加工程序，要求用户输入字符串，然后对字符串进行加工处理。
'''
def process_string(str1:str):
    #一些字符串操作
    str1=str1
    #长度
    n=len(str1)
    #把输入按空格分割成单词
    lst=[word for word in str1.split()]
    #大写
    str2=str1.upper()
    #小写
    str3=str1.lower()
    #首字母大写
    str4=str1.capitalize()
    #每个单词首字母大写
    str5=str1.title()
    #大小写互相转化
    str6=str1.swapcase()
    #把空格用-代替
    str7=str1.replace(" ","-")
    #切片
    str8=str1[0:n:2]
    #取得unicode编码并连接
    unicode_list=[f"\\u{ord(char):04x}" for char in str1]
    unicode_string=''.join(unicode_list)


    #输出
    print("原字符串：",str1)
    print("字符串长度：",n,end='\n')
    print("大写：",str2,end='\t')
    print("小写：",str3,end='\v')
    print(r"\首字母大写\：",str4)
    print("\"每个单词首字母大写\"：",str5)
    print("大小写互转：{0}".format(str6))
    print(f"替换空格：{str7}".center(30))
    print("将源字符串按单词形式输出：",lst)
    print(f"按偶数切片：{str8}")
    print("unicode\u7f16\u7801：",unicode_string)



if __name__ == '__main__':
    process_string("Hello World!")