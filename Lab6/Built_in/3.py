string = str(input("Write something: "))
def func(string):
    r_string = ''.join(reversed(string))
    if(r_string == string):
       print("It's a palindrome")
    else:
        print("It's not a palindrome")
func(string)