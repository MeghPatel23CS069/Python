# Create a Student class with attributes for name, age, and grades, and methods to calculate the average grade and display student information.

class Student :
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades

    def display(self) :
        print("Name :",self.name)
        print("Age :",self.age)
        print("\nMarksheet")

        for subject,marks in self.grades.items() :
            print(f"{subject} : {marks}")

        print("\nAverage grades :",self.average_grades())

    def average_grades(self) :
        return sum(self.grades.values())/len(self.grades.values())
    
marks={"Maths":85,"C++":90,"Java":95,"Python":96}

s=Student("Megh",19,marks)
s.display()

# Create a BankAccount class with attributes for account number, balance, and account type, and methods to deposit, withdraw, and display account information.
print("\n")

class Bank_Account :
    def __init__(self,acc_no,balance,acc_type) -> None:
        self.acc_no=acc_no
        self.balance=balance
        self.acc_type=acc_type
    
    def deposit(self,amount) :
        if amount<=0 :
            print("Please enter correct amount")
        else :
            self.balance+=amount
            print(f"Transaction Succesful \nYour balance is {self.balance}")

    def withdraw(self,amount) :
        if amount>=0 and amount<=self.balance :
            self.balance-=amount
            print(f"Transaction Succesful \nYour balance is {self.balance}")
        else :
            print("Please enter correct amount")

    def display(self) :
        print("Account number :",self.acc_no)
        print("Account type :",self.acc_type)
        print("Current Balance :",self.balance)



account = Bank_Account(101, 5000, "Savings")
account.deposit(1500)
account.withdraw(2000)
account.withdraw(10000)
account.deposit(-500)
print()
account.display()




