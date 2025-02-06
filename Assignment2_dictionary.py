#  Write a program to count the frequency of each word in a string and store it in count phoneionary.
def frequency_count() :
    str="##ddfgtdff.."
    char_frequency={}

    for i in str :
        count=char_frequency.setdefault(i,0)
        count=count+1
        char_frequency[i]=count

    print("String : ",str)

    for keys , values in char_frequency.items() :
        print(f"{keys} : {values}")
    return None

frequency_count()

# Implement a simple phonebook application using a dictionary where users can add, delete, and search for contacts.
print("\n")

phone={}

def add(name,contact) :
    phone[name]=contact
    
def delete(name):
    del phone[name]
    
def search(name) :
    try :
        return phone[name]
    except KeyError :
        return "Contact not found"
        
def show() :
    print("Phone book")
    for keys , values in phone.items() :
        print(f"{keys} : {values}")

add("Megh",123456789)
add("Sir",1122334455)
show()
delete("Sir")
show()
print("Search")
print("Megh :",search("Megh"))
print("Sir :",search("Sir"))


# Create a dictionary of students and their grades. Write a program to filter students who scored more than a specific mark.
print("\n")

result ={
    "Megh" : 69 ,
    "Nisarg" : 70 ,
    "Tejas" : 19 ,
    "Kevin" : 29 ,
    "Aum" : 35
}
passed = []

for items in result.keys() :
    if result[items] >=35 :
        passed.append(items)

print("Result :",result)
print("Passsed students :",passed)

# Write a program to convert a list of tuples (key-value pairs) into a dictionary and vice versa.
print("\n")

List=[("A","a"),("B","b"),("C","c"),("D","d")]

print("List : ",List)

Dict={}

for i in List :
    Dict[i[0]]=i[1]

print("Dictionary : ",Dict)