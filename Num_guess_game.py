print("Hello Folks - This is Number guessing game:")
print("_________________")

import random
print("easy is between 1 and 25")
print("medium is between 1 and 100")
print("hard is between 1 and 200")
dif=input("Choose your difficulty by typing 'e' for easy 'm' for medium and 'h' for hard:-")
while True:
    if dif !="e" or "m" or "h":
        print("Please type again as you have typed an invalid text\n")
        dif=input("Choose your difficulty by typing 'e' for easy 'm' for medium and 'h' for hard:-\n")
    if dif =="e" or "m" or "h":
        if dif=="e":
            num=random.randint(1,25)
            print("So you have chosen easy difficulty")
            break
        if dif=="m":
            num=random.randint(1,100)
            print("So you have chosen medium difficulty")
            break
        if dif=="h":
            num=random.randint(1,200)
            print("So you have chosen hard difficulty")
            break
loopCounter=0
while True:
    
    inputValue=int(input("Guess the number here->  "))
    loopCounter=loopCounter+1
    if num<inputValue:
        print("Try lower")
    if num>inputValue:
        print("Try higher")
    if num==inputValue:
        print("Congratulations, you got it")
        break
print("Your tries: ",loopCounter)