'''
编写一个深度优先搜索函数，生成对于依次抛给定数目的硬币，其正反面情况的可能排列
'''

#定义了一个函数
def generate_cases(n):
    #在函数内部定义了一个子函数
    def dfs(depth,case):
        if depth==n:
            #res是可变对象，我只需要在原地更改res的内容
            res.append(case)
            #引用了子函数作用域外的变量cnt，以免在接下来的编译中系统在子函数的内部重新指派一个cnt
            nonlocal cnt
            #cnt是不可变对象，我需要新建一个空间给cnt+1然后再把cnt的引用指向cnt+1对应的空间
            cnt+=1
            case=[]
            #使用了一下递归
        elif depth<=n:
            dfs(depth+1,case+[0])
            dfs(depth+1,case+[1])

    cnt=0
    res=[]
    #引用子函数
    dfs(0,[])
    print("共{0}种可能排列：{1}".format(cnt,res))
    return

def main():
    n = int(input("请输入硬币数目:"))
    #引用函数
    generate_cases(n)
    return

if __name__=='__main__':
    main()
