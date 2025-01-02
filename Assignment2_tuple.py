# problem 1

def remove_duplictae(input_tuple) :
    return set(input_tuple)

input_tuple = (1,2,3,4,5,6,5,6,8,8,9,7,7,3)
output_tuple=remove_duplictae(input_tuple)

print("Input :",input_tuple)
print("Output :",output_tuple)

# problem 2
print("\n")

students = [(69,"Megh"),(100,"Rishi") ,(19,"Dhruv") , (70,"Nisarg") , (55,"Jay"), (1,"Vijay")]
print("Student list :",students)
students.sort()
print("Sorted list according to marks :",students)

# problem 3
print("\n")

from collections import Counter

sample_tuple = (1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,66,99,66,99)
print("Sample tuple :",sample_tuple)

element_frequency = Counter(sample_tuple)

print("The frequency of elements ")

for elements,count in element_frequency.items() :
    print(f"Element : {elements}  count : {count}")


# problem 4
print("\n")

Records = [ (1,"John Doe",85) , (2,"Megh",69) , (3,"Dhruv",55) , (4,"Kevin",80) ,(5,"Nisarg",70) ]

def search_by_id(id) :
    for record in Records :
        if record[0]==id :
            return record
    return None 

def search_by_name(name) :
    for record in Records :
        if record[1].lower() == name.lower() :
            return record
    return None

def search_by_marks(marks) :
    for record in Records :
        if record[2]==marks :
            return record
    return None

print("Record with id 4 :",search_by_id(4))
print("Record with id 9 :",search_by_id(9))
print("Record with name Megh :",search_by_name("Megh"))
print("Record with name XYZ :",search_by_name("XYZ"))
print("Record with marks 69 :",search_by_marks(69))
print("Record with marks 99 :",search_by_marks(99))