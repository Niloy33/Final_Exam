class Account:
    def __init__(self,name,email,address,account_type) -> None:
        self.name =name
        self.email =email
        self.address =address
        self.account_type =account_type
        self.balance =0
        self.account_no=None
        self.transaction=[]
        self.loan_taken=0

    def deposit(self,amount):
        self.balance+=amount
        print()
        print("Money deposited succesfully")
    
    def withdraw(self,amount,bank):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
            self.transaction.pop()
        else:
            self.balance -= amount
            bank.total_balance -= amount
            print(f'Here is your money {amount}')
            print(f'your balance after withdraw: {self.balance}')
            
    def available_balance(self):
        print(f'Your available balance is: {self.balance}')
    
    def transaction_history(self):
        print("Your transaction history is!!")
        print()
        for i in self.transaction:
            print(i)
    def all_account_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account type: {self.account_type}")
        print(f"Account no: {self.account_no}")
        print(f"Total balance: {self.balance}")

class Bank:
    def __init__(self,name,total_balance) -> None:
        self.name=name
        self.total_balance=total_balance
        self.total_loan=0
        self.loan_status=True
        self.account_list=[]
    def create_account(self,account):
        self.account_list.append(account)
        account.account_no=f'{account.name}{len(self.account_list)+10}'
        print(f'Account created succesfully and your account_no is:- {account.account_no} ')
    
    def bank_deposit(self,account_no,amount):
        account =self.find_account(account_no)
        if account:
            account.deposit(amount)
            account.transaction.append(f'{amount} had been deposited')
            self.total_balance+=amount
        else:
            print("Account does not exist")
        
    def bank_withdraw(self,account_no,amount):
        account =self.find_account(account_no)
        if account:
            if self.total_balance > amount:
                account.transaction.append(f'{amount} has been withdrawed from my account')
                account.withdraw(amount,self)
                
            else:
                print("The bank is bankrupt")
        else:
            print("Account does not exist")
    def loan_taken(self,account_no,amount):
        account =self.find_account(account_no)
        if account:
            if self.total_balance > amount and account.loan_taken < 2 and self.loan_status==True:
                account.deposit(amount)
                account.transaction.append(f'{amount} had been loaned from bank')
                self.total_loan+=amount
                self.total_balance-=amount
                account.loan_taken += 1
                print("Bank has granted your Loan")
            else:
                print("You can't take a loan")
        else:
            print("Account does not exist")
    
    def transfering_to_another_account(self,sender_account_no,receiver_account_no,amount):
        sender_account= self.find_account(sender_account_no)
        receiver_account= self.find_account(receiver_account_no)
        if sender_account and receiver_account:
            if amount > sender_account.balance:
                print("You don't have enough money to transfer")
            else:
                sender_account.balance-=amount
                receiver_account.balance+=amount
                sender_account.transaction.append(f'{amount} has been transfered to account_no: {receiver_account_no}')
                receiver_account.transaction.append(f'Account no {sender_account_no}, transfered {amount} money to my account')
                print(f'{amount} has been transfered to  account_no: {receiver_account.account_no}')
        else:
            print("Account does not exist")

    def balance_of_a_user(self,account_no):
        account =self.find_account(account_no)
        if account:
           account.available_balance()
        else:
            print("Account does not exist")

    def transaction_history_of_a_user(self,account_no):
        account =self.find_account(account_no)
        if account:
           account.transaction_history()
        else:
            print("Account does not exist")
    def bank_total_balance(self):
        print(f'Bank total balance is {self.total_balance}')
    
    def bank_total_given_loan(self):
        print(f'Total given loan to customer is {self.total_loan}')
    
    def on_loan(self):
        self.loan_status=True
        print("Loan has been turned on succesfully")
    
    def off_loan(self):
        self.loan_status=False
        print("Loan has been turned of succesfully")

    def find_account(self,account_noo):
        for account in self.account_list:
            if account.account_no.lower() == account_noo.lower():
                return account
        return None  
    
    def show_all_accounts(self):
        if self.account_list:
            for account in self.account_list:
                print(f'Account details of ${account.name}$:- ')
                account.all_account_details()
                print("---------*****---------")
        else:
            print("Accounts not available")
    def delete_account(self,account_no):
        account =self.find_account(account_no)
        if account:
            print(f'{account.account_no} , Account has been deleted succesfully')
            self.total_balance-=account.balance
            self.account_list.remove(account)
        else:
            print("Account does not exist")

class Admin:
    def __init__(self,name) -> None:
        self.name=name
    def Create_account(self,bank,account):
        bank.create_account(account)
    def Delete_account(self,bank,account_no):
        bank.delete_account(account_no)
    def All_account(self,bank):
        bank.show_all_accounts()
    def Total_bank_balance(self,bank):
        bank.bank_total_balance()
    def Total_loan_amount(self,bank):
        bank.bank_total_given_loan()
    def On_the_loan(self,bank):
        bank.on_loan()
    def Off_the_loan(self,bank):
        bank.off_loan()


bank = Bank("Mamar Restaurement",10000)
def user():
    name = input("Enter Your Name : ")
    
    while True:
        print()
        print(f"Welcome {name}!!")
        print("1. Create your account")
        print("2. Deposit to a account")    
        print("3. Withdraw from a account")    
        print("4. Check available balance of a account")
        print("5. check transaction history of a account.")
        print("6. Take a loan form bank")
        print("7. Transfer money to other account")
        print("8. Exit")
        print()
        
        choice = int(input("Enter Your Choice : "))
        print()
        if choice == 1:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            account_type= input("Enter Your account_type : ")
            print()
            account = Account(name,email,address,account_type)
            bank.create_account(account)

        elif choice == 2:
            account_no = input("Enter account no : ")
            amount = int(input("Enter your amount : "))
            print()
            bank.bank_deposit(account_no,amount)

        elif choice == 3:
            account_no = input("Enter account no : ")
            amount = int(input("Enter your amount : "))
            print()
            bank.bank_withdraw(account_no,amount)
        elif choice == 4:
            account_no = input("Enter account no : ")
            print()
            bank.balance_of_a_user(account_no)
        elif choice == 5:
            account_no = input("Enter account no : ")
            print()
            bank.transaction_history_of_a_user(account_no)

        elif choice == 6:
            account_no = input("Enter account no : ")
            amount = int(input("Enter your amount : "))
            print()
            bank.loan_taken(account_no,amount)
        elif choice == 7:
            sender_account_no = input("Enter sender account no  : ")
            receiver_account_no = input("Enter receiver account no : ")
            amount = int(input("Enter your amount : "))
            print()
            bank.transfering_to_another_account(sender_account_no,receiver_account_no,amount)
        elif choice==8:
            break
        else:
            print("Invalid Input")


def admin():
    name = input("Enter Your Name : ")
    pas=int(input("Enter your password: "))
    admin=Admin(name)
    if pas==22:
        while True:
            print()
            print(f"Welcome {name}!!")
            print("1. Create an account")
            print("2. Delete an account")    
            print("3. View all account list")    
            print("4. Check total available balance of a bank")
            print("5. Check total loan amount of a bank.")
            print("6. Turn off the loan")
            print("7. Turn on the loan")
            print("8. Exit")
            print()
            choice = int(input("Enter Your Choice : "))
            print()
            if choice == 1:
                name = input("Enter Your Name : ")
                email = input("Enter Your Email : ")
                address = input("Enter Your Address : ")
                account_type= input("Enter Your account_type : ")
                account = Account(name,email,address,account_type)
                print()
                admin.Create_account(bank,account)

            elif choice == 2:
                account_no = input("Enter account no : ")
                print()
                admin.Delete_account(bank,account_no)

            elif choice == 3:
                admin.All_account(bank)

            elif choice == 4:
                admin.Total_bank_balance(bank)

            elif choice == 5:
                admin.Total_loan_amount(bank)

            elif choice == 6:
                admin.Off_the_loan(bank)

            elif choice == 7:
                admin.On_the_loan(bank)

            elif choice == 8:
                break
            else:
                print("Invalid Input")
    else:
        print("Wrong password")
    
while True:
    print()
    print("Welcome!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    print()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        user()
    elif choice == 2:
        admin()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")