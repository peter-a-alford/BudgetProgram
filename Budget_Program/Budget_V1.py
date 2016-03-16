#First iteration of my budget program including a total and basic increase
#and decrease of that total.

#menu function
def menu(total):
    while True: #loop to run the menu function
        option = input("Choose from the following options \n" 
               "Option D: to display \n" 
               "Option I: to add income \n" 
               "Option E: to add exspenses \n" 
               "Option Q: to quit \n")
        if(option=='d' or option=='D'): #displaying total cash
            total=display(total)
        elif(option=='i' or option=='I'): #total cash plus new income
            total=add_Income(total)
        elif(option=='e' or option=='E'): #total cash minus expenses
            total=add_Expenses(total)
        elif(option=='q' or option=='Q'): #ending the function
            total=end(total)
            return total 
        else:
            print ("Sorry invalid option")
            
#display function           
def display(total):
    print("Total Cash: " + str(total))
    return total

#add incomce function
def add_Income(total):
    income = int(input("What is your income? "))
    total=(total+income)
    display(total)
    return total

#add expenses function
def add_Expenses(total):
    exspenses = int(input("What are you exspenses? "))
    total = (total-exspenses)
    display(total)
    return total

#quit function
def end(total):
    return total

#main function
total = int(input("What is your total income: "))
total = menu(total) #calling the menu function which runs the main function.
