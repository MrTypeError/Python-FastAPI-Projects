'''
If Else Assignment

- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

'''

def grade_provider(user_score) :
    if user_score <= 100 and user_score >= 90 :
        return "Grade A"
    elif user_score < 90 and user_score >= 80 :
        return "Grade B"
    elif user_score < 80 and user_score >= 70 :
        return "Grade C"
    elif user_score < 70 and user_score >= 60 :
        return "Grade D"
    else :
        return "Need to study more buddy!!"

user_inp_name = input("Enter the Name of the Student : ")
user_inp_score = int(input("Enter the Score that the student has got : "))

print(grade_provider(user_inp_score))
