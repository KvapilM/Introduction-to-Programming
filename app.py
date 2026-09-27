name = input("Write your username: ")

loopContinue = False

while(loopContinue == False):
    choice = input("Do you want 1-Normal greeting or 2-Formal greeting: ")

    if(choice == "1"):
        print("Wassup " + name)
        loopContinue = True
    if(choice == "2"):
        print("Good morning sir " + name)
        loopContinue = True
