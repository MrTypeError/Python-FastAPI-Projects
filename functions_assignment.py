'''
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values

'''


def dict_maker(fname , lname , age) :
    user_identity = {}
    user_identity["Firstname"] = fname
    user_identity["Lastname"] = lname
    user_identity["Age"] = age

    return user_identity


fname = input("Enter the Firstname of the user : ")
lname = input("Enter the Lastname of the user : ")
age = int(input("Enter the age of the user : "))
#function call 
print(dict_maker(fname , lname , age))
