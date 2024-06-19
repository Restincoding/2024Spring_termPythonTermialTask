'''
编写了一个基础的银行程序, 有基础账户和投资账户两个类
'''
class BankAccount:
    """
    基础账号类
        属性：账号，持有者，余额
        方法：存款，取款，查询余额
    """
    #初始化方法
    def __init__(self,account_number,account_holder,account_balance=0):
        self.account_number=account_number#账号
        self.account_holder=account_holder#持有者
        self.account_balance=account_balance#账户余额
        print(f"创建账户{self.account_number}成功, 持有者{self.account_holder}, 初始余额{self.account_balance:.2f}元")

    #存款方法
    def deposit(self,amount):
        if amount>0:
            self.account_balance+=amount
            print(f"{self.account_holder}向{self.account_number}存款{amount}元")
        else:
            print("无效的存款金额")

    #取款方法
    def withdraw(self,amount):
        if amount>0:
            self.account_balance-=amount
            print(f"{self.account_holder}从{self.account_number}取款{amount}元")
        else:
            print("无效的取款金额")

    #查询余额方法
    def display_balance(self):
        print( f"{self.account_holder}名下的账户{self.account_number}的余额为:{self.account_balance:.2f}元")

    #析构函数
    def __del__(self):
        print(f"账户{self.account_number}被销毁")


#继承        
class InvestmentAccount(BankAccount):
    '''
    投资账户类
        继承BankAccount类, 添加了计算投资收益的方法
        属性：年利率
        方法：计算收益
    '''
    #覆盖父类的__init__方法
    def __init__(self, account_number, account_holder, initial_balance=0,annual_interest_rate=0):
        #使用super函数调用父类的初始化方法
        super().__init__(account_number, account_holder, initial_balance)
        #另外初始化年利率
        self.annual_interest_rate = annual_interest_rate

    #计算利息方法
    def calculate_interest(self,years):
        if self.annual_interest_rate>0:
            final_amount=self.account_balance*(1+self.annual_interest_rate/100)**years
            self.account_balance=final_amount
            print(f"经过{years}年, 账户{self.account_number}余额: {self.account_balance:.2f}")
        else:
            print("无效年利率")


#多态
class SavingAccount(BankAccount):
    '''
    储蓄账户类
        继承BankAccount类, 添加了计算利息的方法
        属性：日利率，默认为%
        方法：计算利息
    '''
    def __init__(self, account_number, account_holder, initial_balance=0,daily_interest_rate=1):
        #使用super函数调用父类的初始化方法
        super().__init__(account_number, account_holder, initial_balance)
        #把日利率设为私有变量
        self._daily_interest_rate = daily_interest_rate
    

    def calculate_interest(self,days):
        if days>0:
            final_amount=self.account_balance*(1+self._daily_interest_rate/100)**days
            self.account_balance=final_amount
            print(f"经过{days}天, 账户{self.account_number}余额: {self.account_balance:.2f}")
        else:
            print("无效储存日期")



if __name__=="__main__":
    #创建一个基础账户
    account1=BankAccount("123456789","李华",1000)
    account1.withdraw(500)
    account1.display_balance()
    account1.deposit(200)
    account1.display_balance()


    #创建一个投资账户
    account2=InvestmentAccount("987654321","小明",1000,5)
    account2.calculate_interest(3)
    account2.withdraw(500)
    account2.display_balance()

    #创建一个储蓄账户
    account3=SavingAccount("321654987","小红",1000)
    account3.calculate_interest(30)
    account3.display_balance()