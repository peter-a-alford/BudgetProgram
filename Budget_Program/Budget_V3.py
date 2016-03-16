#Third iteration of my budge program
#Changed the format of the history storage from parses information to a single string.
#Added code to filter out bad responses
#

import datetime

def menu(total, history):
    while True: 
        option = input("\nChoose from the following options \n" 
               "Option D: to display \n" 
               "Option I: to add income \n" 
               "Option E: to add exspenses \n" 
               "Option Q: to quit \n")
        if(option=='d' or option=='D'): 
            total=display(total, history)
        elif(option=='i' or option=='I'): 
            total=add_Income(total, history)
        elif(option=='e' or option=='E'): 
            total=add_Expenses(total, history)
        elif(option=='q' or option=='Q'): 
            total=end(total, history)
            return total 
        else:
            print ("Sorry invalid option")
                     
def display(total, history):
    print("Total Cash: " + str(total))
    print("History of Expenses/Income")
    if not history:
        print("N/A")
    else:
        for x in range(len(history)):
              print(str(x+1) + " " + history[x])
    return total

def add_Income(total, history):
    while True:
        try:
            income = float(input("What is your income? "))
        except ValueError:
            print("Bad input")
            continue
        else:
            break
    time=datetime.datetime.today().strftime("%H:%M:%S%p %m/%d/%Y")
    history_entry=(str(time) + " " + "Income: $" + str(income))
    history.append(history_entry)
    total=(total+income)
    return total

def add_Expenses(total, history):
    while True:
        try:
            expenses = float(input("What is you expense? "))
        except ValueError:
            print("Bad input")
            continue
        else:
            break    
    time=datetime.datetime.today().strftime("%H:%M:%S%p %m/%d/%Y")
    history_entry=(str(time) + " " + "Expense: $" + str(expenses))
    history.append(history_entry)
    total = (total-expenses)
    return total

def end(total, history):
    file=open('/Users/Mask/Desktop/Budget_Program/budgetHistory.txt', 'w')
    for x in range(len(history)):
        file.write(history[x]+'\n')
        file.write(total)
    return total

budget_history=open('/Users/Mask/Desktop/Budget_Program/budgetHistory.txt', 'r').readlines()
total=budget_history[len(budget_history)]
budget_history.pop(len(budget_history))
total = menu(total, budget_history)

#***comments***
#create a buffer for the file I/O.
