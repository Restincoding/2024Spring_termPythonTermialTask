"""
一个加减乘除计算器，利用异常处理机制检验输入是否合法
"""

def perform_operation(a,b,operation):
    try:
        if operation=='+':
            result=a+b
        elif operation=='-':
            result=a-b
        elif operation=='*':
            result=a*b
        elif operation=='/':
            #检查除数是否为0
            if b==0:
                raise ValueError("错误：除数不能为0")
            result=a/b
        else:
            raise ValueError("错误：无效的操作符")
        return result
    except ValueError as ve:
        return ve

def main():
    print("简单计算器：支持 +, -, *, / 运算")
    num1=input("请输入第一个数字：")
    num2=input("请输入第二个数字：")
    operation=input("请输入操作符：")

    #尝试将输入转换为浮点数
    try:
        num1=float(num1)
        num2=float(num2)
    except ValueError:
        print("错误：请确保输入的是有效的数字。")
        return

    # 执行运算并处理结果
    result=perform_operation(num1, num2, operation)
    print(result)

if __name__=="__main__":
    main()