import random
a = random.randrange(1, 20)
def guess_number(rand):
    b = str(input("Hello! What is your name? "))
    print("Well, " + b + ", I am thinking of a number between 1 and 20. ")
    num = int(0)
    c = int(input("Take a guess. "))
    while(True):
        if(c < rand):
            print("Your guess is too low.")
            c = int(input("Take a guess. "))
            num += 1
        elif(c > rand):
            print("Your guess is too high.")
            c = int(input("Take a guess. "))
            num += 1
        elif(c == rand):
            num += 1
            print("Good job, " + b + "! You guessed my number in ", end = "")
            print(num, end = "")
            print(" guesses!")
            exit()
guess_number(a)