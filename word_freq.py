def word_frequency(text):
    res = {key: text.count(key) for key in text.split()}
    print("The words frequency : " + str(res))
if __name__ == "__main__":
    text = str(input("Enter the string :"))
    word_frequency(text= text.lower())
