def power(x, y):
    return x ** y

yes = "yes" or "Yes"
print ("This is for Indicies")
def main():
    while True:
        first = int(input("Give me one number: "))
        second = int(input("give me a second number: "))
        answerOne = "yes" or "Yes"
        answerTwo = "no" or "No"
        

        if input("Would you like your answer ") == answerOne:
            print (first, "to the power of ", second, "equals: ", power(first, second))
            again = input("Would you like to use the calculator again? Enter yes or no: ")
            if again == answerTwo:
                    print ("Thanks for using!")
                    return
            elif again == answerOne:
                    print ("Lets do it again..")
            else:
                    print ("You should enter either \"yes\" or \"no\".")
             
        else:
             print ("Goodbye")
             kill()
if __name__ == "__main__":
    main()

                
    
