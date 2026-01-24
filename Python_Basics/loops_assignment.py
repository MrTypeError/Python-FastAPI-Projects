'''

Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

- Create a while loop that prints all elements of the my_list variable 3 times.

- When printing the elements, use a for loop to print the elements

- However, if the element of the for loop is equal to Monday, continue without printing

'''

# Solution

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

n = len(my_list)
i = 0
while i < n : 
    for j in range(0,3) :
        if my_list[i] != "Monday" :
            print(my_list[i])
    i+=1
