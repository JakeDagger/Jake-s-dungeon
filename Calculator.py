def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def power(x, y):
   return x ** y


def main():
    while True:
        print("Select calculator function please.")
        print("1 = Add")
        print("2 = Subtract")
        print("3 = Multiply")
        print("4 = Divide")
        print("5 = Indicies")

        choice = input("Enter choice 1, 2, 3, 4 or 5: ")
        answerOne = ("y" or "Y")
        answerTwo = ("n" or "N")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
            again = input("Would you like to use the calculator again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")

        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))
            again = input("Would you like to use the calculator again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")

        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))
            again = input("Would you like to use the calculator again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")
                    
        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
            again = input("Would you like to use the calculator again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")

        elif choice == '5':
            print(num1,"to the power of ",num2,"=", power(num1,num2))
            again = input("Would you like to use the calculator again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")
                    
        else:
            print("Invalid input")
            again = input("Would you like to try again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")
                    again = input("Would you like to try again? Enter y/n: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"y\" or \"n\".")
                    kill()
if __name__ == "__main__":
    main()
