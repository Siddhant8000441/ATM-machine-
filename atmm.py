class ATM:
    def __init__(self):
        print(id(self))
        self.balance = 0
        self.pin = ''

    def menu(self):
        user_input = input("""Welcome to the ATM
              
              1. Press 1 to Create Your Pin
              2. Press 2 to Change Your Pin
              3. Press 3 to Check Your Balance
              4. Press 4 to Withdraw
              5. Press 5 for Anything Else to Exit
              """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter Your Pin: ")
        self.pin = user_pin
        print("Pin Created Successfully")

        user_balance = int(input("Enter Your Balance: "))
        self.balance = user_balance
        print("Balance Added Successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter Your Old Pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter Your New Pin: ")
            self.pin = new_pin
            print("Pin Changed Successfully")
        else:
            print('Incorrect Pin, Operation Failed')
        self.menu()

    def check_balance(self):
        print("Your Current Balance is", self.balance)
        self.menu()

    def withdraw(self):
        user_pin = input('Enter the Pin: ')
        if user_pin == self.pin:
            amount = int(input('Enter the Amount: '))
            if amount <= self.balance:
                self.balance -= amount
                print('Withdrawal Successful. Balance is', self.balance)
            else:
                print('Insufficient Balance')
        else:
            print('Incorrect Pin')
        self.menu()

# Create an instance of the ATM class
obj = ATM()
obj.menu()
