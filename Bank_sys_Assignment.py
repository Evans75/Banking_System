class Bank():
    def __init__(self,Bankid,Name,Location):
        assert type(Bankid)== int and type(Location)== str
        self.Bankid = Bankid
        self.Name = Name
        self.Location=Location
BankA = Bank(1,'STANBIC','KAMPALA')
BankB = Bank(2,'EXIM','JINJA')

class Teller_1(Bank):
    def __init__(self,Id,Name):
        assert type(Id) == int
        self.Id = Id
        self.Name = Name
        self.balance = 0


    def CollectMoney(self,amount):
        self.balance += amount#whenever deposit is done,it is added to the remaining balance
        return self.balance

    def OpenAccount(self):#enable direct entry
        print("%d %s your account number is %d")
        print("your branch is%s"%BankA.Location)

    def CloseAccount(self):#enable delete
        print("%s your account is closed")
        print("your branch is %s"%BankA.Location)
    def Loanrequest(self):
        if self.balance > 4000:#enable ask amount
            print("you are legible to getting a loan")
            print("your branch is %s"%BankA.Location)
        else:
            print("request failed")
            print("your branch is %s"%BankA.Location)

    def ProvideInfo(self):#enable print all detail
        print("Id:%d,Name:%s,Address:%s,PhoneNo:%d,AccNo:%d   ")
        print("your branch is %s"%BankA.Location)

    def IssueCard(self):#enable card number
        print("%s, your ATM is ready"%self.Name)
        print("your branch is %s"%BankA.Location)



class Teller_2(Bank):#looking for a possibility of using a dictionary
    def __init__(self,Id,Name):
        assert type(Id) == int
        self.Id = Id
        self.Name = Name
        self.balance = 0

    def CollectMoney(self,amount):
        self.balance += amount
        return self.balance

    def OpenAccount(self):
        print("%d %s your account number is %d")
        print("your branch is%s"%BankB.Location)

    def CloseAccount(self):
        print("%s your account is closed")
        print("your branch is %s"%BankB.Location)

    def Loanrequest(self):
        if self.balance >= 1000:
            print("you are legible to getting a loan")
            print("your branch is %s"%BankB.Location)
        else:
            print("request failed")
            print("your branch is %s"%BankB.Location)

    def ProvideInfo(self):
        print("Id:%d,Name:%s,Address:%s,PhoneNo:%d,AccNo:%d   ")
        print("your branch is %s"%BankB.Location)

    def IssueCard(self):
        print("%s, your ATM is ready"%self.Name)
        print("your branch is%s"%BankB.Location)
        print("you were served by %s"%Evans.Name)






class CustomerB(Teller_2,Bank):
    def __init__(self,Id,Name,Address,PhoneNo,AccNo,Balance):


       self.Id = Id
       self.Name = Name
       self.Address = Address
       self.PhoneNo = PhoneNo
       self.AccNo = AccNo
       self.balance = Balance


    def GeneralInquiry(self):
        print("Id:%d,Name:%s,Address:%s,PhoneNo:%d,AccNo:%d,Balance:%d"%(self.Id,self.Name,self.Address,self.PhoneNo,self.AccNo,self.balance))

    def DepositMoney(self,amount):
        assert type(amount) == int

        self.balance += amount

        print('%d is your balance'%(self.balance))


    def WithdrawMoney(self,amount):
        self.balance -= amount
        print("%d is your balance"%(self.balance))


    def openAccount(self):
        print("Do you wish to open an account")


    def closeAccount(self):#enable del account
        print("Your account nolonger exist")


    def applyLoan(self):#enable data entry
        print("Name:%d,AccNo:%d I would like to get a loan")

    def requestCard(self):#print card number
        print("where is my card")

class CustomerA(Teller_1,Bank):
    def __init__(self,Id,Name,Address,PhoneNo,AccNo,Balance):

        #looking for a possibility of using a dictionary for this purpose
       self.Id=Id
       self.Name=Name
       self.Address=Address
       self.PhoneNo=PhoneNo
       self.AccNo=AccNo
       self.balance=Balance


    def GeneralInquiry(self):#print bank location too
        print("Id:%d,Name:%s,Address:%s,PhoneNo:%d,AccNo:%d,Balance:%d"%(self.Id,self.Name,self.Address,self.PhoneNo,self.AccNo,self.balance))

    def DepositMoney(self,amount):
        assert type(amount) == int

        self.balance += amount
        #add you deposited.....
        print('%d is your balance'%(self.balance))


    def WithdrawMoney(self,amount):
        self.balance -= amount
        print("%d is your balance"%(self.balance))


    def openAccount(self):
        print("Do you wish to open an account")


    def closeAccount(self):
        print("Your account nolonger exist")


    def applyLoan(self):
        print("Name:%d,AccNo:%d I would like to get a loan")

    def requestCard(self):
        print("where is my card")
        print("you were served by %s"%Teller_1.Name)


Evans = Teller_1(7,"Ochieng")

ochieng = CustomerB(15,"Evans","Kampala",5000,190,0)
print(ochieng.GeneralInquiry())
ochieng.DepositMoney(5000)
ochieng.Loanrequest()
ochieng.IssueCard()

Arthur = CustomerA(17,"Linard","Jinja",23002,360,0)
print(Arthur.GeneralInquiry())
Arthur.IssueCard()

