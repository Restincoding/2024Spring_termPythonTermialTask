'''
编写了一个质数判断程序，其中使用了顺序、循环、选择三种控制结构
'''
import typing
def check_prime(n:int)->None:
    #出现了单分支选择结构
        #出现了逻辑运算符
    if n==0 or n==1:
        print("{0}不是个质数".format(n))
        return
    #出现了for引导的循环结构
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("{0}不是个质数".format(n))
            return
    print("{0}是个质数".format(n))
    return 

def check_nn(n,max_val=2**31-1)->typing.Union[int,None]:
    try:
        n=int(n)
        #出现了多分支选择结构
        if n<0:
            raise ValueError
        elif n>max_val:
            raise ValueError
        return n
    except ValueError:
        print("无效输入，请重新输入")
        return None


def main():
    n=input("本程序可以判定一个0到2**31-1范围内的自然数是不是质数。请输入一个待判定的自然数：")
    num=check_nn(n)
    if num:
        check_prime(num)

if __name__=='__main__':
    main()