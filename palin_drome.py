def is_palindrome(text):
    if text==text[::-1]:
        print(text ,"Is palindrome")
    else:
        print(text , "is not palindrome")
if __name__== "__main__":
    text= str(input("Enter the word to be checked for palindrome : "))
    is_palindrome(text=text.lower())