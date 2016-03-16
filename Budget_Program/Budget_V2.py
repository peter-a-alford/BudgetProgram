#Second iteration of my budget program that has an improved display with a history
#of past transactions with timestamps

import datetime #for the purpose of adding timestamps

def menu(total):
    history=[]
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
            total=end(total)
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
              print(str(history[x][2]) + " " + str(history[x][1]) + ": $e" + str(history[x][0]))
    return total

def add_Income(total, history):
    income = float(input("What is your income? "))
    time=datetime.datetime.today().strftime("%H:%M:%S%p %m/%d/%Y")
    history_entry=[income, "Income", time]
    history.append(history_entry)
    total=(total+income)
    return total

def add_Expenses(total, history):
    expenses = float(input("What are you exspenses? "))
    time=datetime.datetime.today().strftime("%H:%M:%S%pi %m/%d/%Y")
    history_entry=[expenses, "Expenses", time]
    history.append(history_entry)
    total = (total-expenses)
    return total

def end(total):
    return total

total = 0
total = menu(total)

#comments
#http://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
