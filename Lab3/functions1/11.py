a = input()
def palindrome(x):
    if(x == x[::-1]):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
palindrome(a)