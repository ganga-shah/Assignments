def ticket_price(age,student):
    if(0<age<=12):
         print("your ticket price is $10")
    elif(12<age<17):
        print("your ticket price is $15")
    elif(17<age and student == student):
        if True:
            print("your ticket price is $18")
        else:
            print("your ticket price is $20")
if __name__ == "__main__":
    age = int(input("Enter the age  :"))
    student = input("Enter the role  :")
    ticket_price(age=age, student=student)
