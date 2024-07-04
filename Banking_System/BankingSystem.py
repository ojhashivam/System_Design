class Bank:
    def __init__(self):
        self.__Balance=0
        self.__pin=""
        self.__pin=int(input("Set Your Pin:"))
        print("PIN Set Successfully!")

        self.menu()
    
    def menu(self):
        print("\nSelect How Do Want To Proceed!!")
        print("Enter 1 To Change Pin:")
        print("Enter 2 To Deposit:")
        print("Enter 3 To Withdraw:")
        print("Enter 4 To Check Balance:")
        print("Ente 5 To Exit!")
        c=int(input())
        if c==1:
            self.changePin()
        elif c==2:
            self.deposit()
        elif c==3:
            self.withdraw()
        elif c==4:
            self.checkBalance()
        elif c==5:
            print("\nThank You!!")
            exit()
        else:
            print("Wrong Input!")
            self.menu()
         

    def changePin(self):
        c=int(input("\nEnter Old Pin:"))
        if c==self.__pin:
            self.__pin=int(input("Enter New Pin:"))
            print("PIN Changed Successfully!")
            self.menu()
        else:
            print("\nWrong Passcode!!")
            self.menu()
    
    def deposit(self):
        if self.pinValidation():
                self.__Balance+=int(input("Enter Amount To Deposit:"))
                print("\nDeposit Successfull!!\nYour Current Balance Is:",self.__Balance)
                self.menu()
        else:
            print("\nWrong Passcode!!")
            self.menu()
    
    def pinValidation(self):
        c=int(input("Enter Pin:"))
        if c==self.__pin:
            return True
        return False
    
    def withdraw(self):
        if self.pinValidation():
            c=int(input("\nEnter Amount To Withdraw:"))
            if c<=self.__Balance:
                self.__Balance-=c
                print("\nTransaction Successfull!!")
                self.menu()
            else:
                print("\nInsufficient Funds!")
                self.menu()
        else:
            print("\nWrong Pin!")
        self.menu()
    
    def checkBalance(self):
        if self.pinValidation():
            print("\nYour Current Balance Is:",self.__Balance)
            self.menu()
        else:
            print("\nWrong Pin!")
            self.menu()
            

if __name__=="__main__":
    Bank()

    
