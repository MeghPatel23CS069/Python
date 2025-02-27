# Write a program to create a class with attributes and methods. 

class T:
    def __init__(self, value):
       self.value = value

    def display(self):
        print(f"Value: {self.value}")

    def update_value(self, new_value):
        self.value = new_value
        print(f"Updated Value: {self.value}")

# Example usage
t1 = T(10)
t1.display()
t1.update_value(20)
t1.display()




# Another example of a class in Python, this time modeling a Bank Account.


class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
       print(f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}")

# Example usage
account1 = BankAccount("Alice", 1000.0)
account1.get_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)




# Write a program to Instantiate an object from a class.

# Defining a class
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city= city

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.I am staying at {self.city}")

# Instantiating an object from the class
person1 = Person("Jigar", 35, "Nadiad")

# Calling a method on the object
person1.introduce()




# Write a program to Access and modify the attributes of an object.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # Dictionary to store subject-wise marks

    def display_marks(self):
        print(f"\nStudent: {self.name}")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def update_marks(self, subject, new_mark):
        if subject in self.marks:
            self.marks[subject] = new_mark
            print(f"Updated {subject} marks to {new_mark} for {self.name}.")
        else:
            print(f"Subject '{subject}' not found!")

# Instantiating an object
student1 = Student("Jigar", {"Math": 85, "Science": 90, "English": 78})

# Displaying marks before modification
print("Before modification:")
student1.display_marks()

# Modifying marks
student1.update_marks("Science", 95)  
student1.update_marks("Math", 88)

# Displaying marks after modification
print("\nAfter modification:")
student1.display_marks()




# Write a program to Call methods defined in a class using an object.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

    def is_pass(self):
        if self.marks >= 40:
            print(f"{self.name} has passed!")
        else:
            print(f"{self.name} has failed.")

# Creating an object of the class
student1 = Student("Jigar", 75)
student2 = Student("Dhaval", 35)

# Calling methods using the object
print("Student 1 Details:")
student1.display_info()
student1.is_pass()

print("\nStudent 2 Details:")
student2.display_info()
student2.is_pass()




# Write a program to Access and modify the attributes of an object using getter and setter methods.

# Defining a class
class Student:
    def __init__(self, name, marks):
        self.__name = name       
        self.__marks = marks    

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter method for marks
    def get_marks(self):
        return self.__marks

    # Setter method for marks
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks! Marks should be between 0 and 100.")

    # Method to display student details
    def display_info(self):
        print(f"Student Name: {self.__name}")
        print(f"Marks: {self.__marks}")

# Creating an object of the class
student1 = Student("Jigar", 85)

# Accessing attributes using getter methods
print("Before Modification:")
print(f"Name: {student1.get_name()}")
print(f"Marks: {student1.get_marks()}")

# Modifying attributes using setter methods
student1.set_name("Dhaval")
student1.set_marks(90)  
student1.set_marks(110) 

# Displaying updated details
print("\nAfter Modification:")
student1.display_info()




# Write a program to Create a subclass that inherits from a superclass.

# Superclass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Subclass inheriting from Person
class Student(Person):
    def __init__(self, name, age, emp_id, marks):
        super().__init__(name, age)  
        self.emp_id = emp_id
        self.marks = marks

    def display_student_info(self):
        self.display_info()  
        print(f"Emp ID: {self.emp_id}, Marks: {self.marks}")

# Creating an object of the Student Class
student1 = Student("Jigar", 35, 676, 85)

# Calling methods
print("Student Details:")
student1.display_student_info()




# Write a program to Override methods in a subclass to provide specific implementations.

# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")

# Subclass overriding the method
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks: Woof! Woof!")

# Subclass overriding the method
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows: Meow! Meow!")

# Creating objects of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the overridden methods
dog.make_sound()
cat.make_sound()




# Write a program to call methods from the superclass using the super() function.

# Superclass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Subclass inheriting from Person
class Student(Person):
    def __init__(self, name, age, emp_ID, marks):
        super().__init__(name, age)  # Calling constructor of superclass
        self.emp_ID = emp_ID
        self.marks = marks

    def display_info(self):
        super().display_info()  # Call display_info() of the superclass
        print(f"Emp ID: {self.emp_ID}, Marks: {self.marks}")

# Creating an object of the Student class
student1 = Student("Jigar", 35, "676", 85)

# Calling the overridden method
print("Student Details:")
student1.display_info()




# Define and use class variables that are shared among all instances of a class. 

class Student:
    school_name = "ABC High School"  # Class variable (shared among all instances)

    def __init__(self, name, grade):
        self.name = name  # Instance variable
        self.grade = grade  # Instance variable

    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")

# Creating objects of the Student class
student1 = Student("Rahul", "10th")
student2 = Student("Aisha", "12th")

# Displaying student details
print("Before modifying class variable:")
student1.display_info()
student2.display_info()

# Modifying the class variable
Student.school_name = "XYZ International School"

# Displaying student details after modification
print("\nAfter modifying class variable:")
student1.display_info()
student2.display_info()




# Define and use instance variables that are unique to each object.

# Defining a class with instance variables
class Student:
    def __init__(self, name, grade, marks):
        """Constructor to initialize instance attributes"""
        self.name = name  # Instance variable (unique to each object)
        self.grade = grade  # Instance variable (unique to each object)
        self.marks = marks  # Instance variable (unique to each object)

    def display_info(self):
        """Method to display student details"""
        print(f"Student Name: {self.name}, Grade: {self.grade}, Marks: {self.marks}")

# Creating objects of the Student class (each with unique values)
student1 = Student("Rahul", "10th", 85)
student2 = Student("Aisha", "12th", 90)

# Displaying student details
student1.display_info()
student2.display_info()




# Create a class that inherit from multiple superclass

# Superclass 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Superclass 2
class Company:
    def __init__(self, company_name, position):
        self.company_name = company_name
        self.position = position

    def display_company_info(self):
        print(f"Company: {self.company_name}, Position: {self.position}")

# Subclass inheriting from both Person and Company
class Employee(Person, Company):
    def __init__(self, name, age, company_name, position, salary):
        Person.__init__(self, name, age)  # Calling Person's constructor
        Company.__init__(self, company_name, position)  # Calling Company's constructor
        self.salary = salary  # New attribute specific to Employee

    def display_employee_info(self):
        self.display_person_info()  # Call method from Person class
        self.display_company_info()  # Call method from Company class
        print(f"Salary: Rs{self.salary}")

# Creating an object of Employee
employee1 = Employee("Rahul", 30, "TechCorp", "Software Engineer", 75000)

# Calling the method to display employee details
print("Employee Details:")
employee1.display_employee_info()

#  Understand and use the method resolution order to determine the order in which base classes are searched.
print("\n")

class A:
    def rk(self):
        print("In class A")

class B:
    def rk(self):
        print("In class B")

# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")

r = C()

# it prints the lookup order 
print(C.__mro__)
print(C.mro())