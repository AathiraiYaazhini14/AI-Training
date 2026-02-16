class Bank:
    def __init__(self,num,name,bal):
        self.num=num
        self.name=name
        self.bal=bal
    def deposit(self,amt):
        self.bal+=amt
        return "Deposited"
    def withdr(self,amt):
        if(amt>=self.bal):
            return "Not possible"
        else:
            self.bal-=amt
            return self.bal
    def display(self):
        print(self.num)
        print(self.name)
        print(self.bal)
num=int(input())
name=input()
bal=int(input())
ban=Bank(num,name,bal)
while True:
    ch=int(input())
    if ch==1:
        amt=int(input())
        print(ban.deposit(amt))
    elif ch==2:
        amt=int(input())
        print(ban.withdr(amt))
    elif ch==3:
        ban.display()
    else:
        break