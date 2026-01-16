'''
Lists Assignment

- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

'''

zoo = ["Dog" , "Elephant" , "Cow" , "Lion" , "Panda"] # Creating a List
print(zoo)

zoo.pop(2) #removing some element from a specific position.
print(zoo)

zoo.append("Gorilla") #appending someting at the end of the list.
print(zoo)

zoo.pop(0) #removing the 1st element of the list.
print(zoo)

#printing all the animals in the zoo
for animal in zoo:
    print(animal) 

#Print only the first 3 animals
for index in range(len(zoo)):
    if index < 3:
        print(zoo[index])
    else:
        break

