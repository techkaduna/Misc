import sys

class Account():
    def __init__(self,owner=" ",balance=0):
        print('''
        
        Welcome to Elytes bank today.''')
        self.owner = str(input("Input your name: "))
        self.balance = float(balance)
        self.trials = 2
        self.pin = '1969'


    def deposit(self,amount=0):
        if self.trials > -1:
            pin = input('Enter pin: ')
            if pin == self.pin:
                amount = input("deposit ammt: ")
                self.balance = self.balance + float(amount)
                print("You just deposited {} to your account".format(amount))
                print(f"Your current balance is "+str(self.balance))
                self.ask_operation()
            else:
                print(f'Incorrect pin. {self.trials} remaining')
                self.trials -= 1
                self.deposit()
        else:
            print('''
            Your account has been blocked for inputing wrong pin thrice.
            Visit our bank branch nearest to you with proof of ownership of account to unblocked your account.
            --Management,Elytes banks plc.
            ''')


    def withdrawal(self,amount=0):
        if self.trials > -1:
            pin = input('Input pin: ')
            if pin == self.pin:
                amount = input("withdraw ammt: ")
                if float(amount) <= self.balance:
                    self.balance = self.balance - float(amount)
                    print(f"You just withdrew "+ str(amount ) + " your new balance is " + str(self.balance))
                else:
                    print("Insufficient fund!")
                self.ask_operation()
            else:
                print(f'Incorrect pin. {self.trials} remaining')
                self.trials -= 1
                self.deposit()
        else:
            print('''
            Your account has been blocked for inputing wrong pin thrice.
            Visit our bank branch nearest to you with proof of ownership of account to unblocked your account.
            --Management,Elytes banks plc.
            ''')

    def ask_operation(self):
        ask = input('Do you want to continue with other transactions--1 = Yes,2 = No: ')
        if ask == '1':
            self.manage()
        elif ask == '2':
            sys.exit()
        else:
            print('Incorrect input')
            self.ask_operation()

    def manage(self):
        print(" Welcome," + self.owner )
        print('What operations do you want to carry out today?')
        user_input = input('''
        press 1 for deposit
        press 2 for withdrawal
        press 3 for account balance 
        press 4 for help service
        press 5 to quit prompt
        ''')
        
        if user_input == '1':
            self.deposit()
        elif user_input == '2':
            self.withdrawal()
        elif user_input == '3':
            print(f"Your account balance is {self.balance} as at today")
            self.ask_operation()
        elif user_input == '4':
            print(" This service is under construction")
            self.ask_operation()
        elif user_input == '5':
            print("Thanks for using Elytes atm service.We hope to see you some other times,Bye.")
            sys.exit()
        else:
            print("Your input wasn't recognized")
            self.manage()        

    def __str__(self):
        return f"{self.owner},your account balance is {self.balance}"


        

if __name__ == "__main__":
    acc1 = Account().manage()
    
