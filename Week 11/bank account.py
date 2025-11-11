class BankAccount:
    rate=0.02
    def __init__(self,name,inital_balance=0):
        self.owner=name
        self.balance=0
    def deposit(self,value):
        self.balance+=value
    def withdraw(self,value):
        if value>self.balance:
            print("insufficient funds")
        else:
            print(f'here is your ${value}.')
            self.balance-=value
    def get_balance(self):
        return self.balance
    def set_balance(self, new_balance):
        self.balance=new_balance
    def get_owner(self,):
        return self.owner
    def set_owner(self,new_owner):
        self.owner=new_owner
    def __str__(self):
        return f'owner: {self.get_owner()}, balance: {self.get_balance()}'
        
    def __add__(self,other):
        new_owner=f'{self.get_owner()} & {other.get_owner()}'
        new_balance=self.get_balance() + other.get_balance()
        new_account=BankAccount(new_owner,new_balance)
        return new_account
    def __eq__(self, other):
        return self.get_owner()==other.get_owner()
    def give_interest(self):
        self.balance=self.balance+self.balance*self.rate

    



        
matt_acc=BankAccount('matt')
matt_acc.deposit(100)
# matt_acc.deposit(50)
# #print(matt_acc.get_balance())

ashley_acc=BankAccount('ashley',500)
ashley_acc.deposit(250)
print(ashley_acc)
ashley_acc.give_interest()
print(ashley_acc)


BankAccount.rate=0.03
ashley_acc.rate=0.02
print(ashley_acc.rate)
# other_acc=BankAccount('???', 100)
# joint_acc=matt_acc+ashley_acc
# print(joint_acc)
# new_acc=joint_acc+other_acc

print(ashley_acc)
ashley_acc.give_interest()
print(ashley_acc)




# print(new_acc)

