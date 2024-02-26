def calculate_grade(score):
    if(100>score>=90):
        print("you have passed in grade A")
    elif(90>score>=80):
        print("you have passed in grade B")
    elif(80>score>=70):
        print("you have passed in grade C")
    elif(70>score>=60):
        print("you have passed in grade c")
    else:
        print("you have received F grade")

if __name__ == "__main__":
    score = int(input("Enter the obtained score  :"))
    calculate_grade(score=score)