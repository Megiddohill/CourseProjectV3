from datetime import datetime # You need datetime to make your date=time functionality

def get_name():
    name = input("What is your name? Enter 'End' to quit: ")
    return name

def get_dates():
    fromdate = input("Enter start date- mm/dd/yyyy: ")
    todate = input("Enter end date- mm/dd/yyyy: ")
    return fromdate, todate

def get_hours():
    hours = int(input("Enter hours worked this week: ")) #Create a function that will input and return total hours and is called inside the loop.
    return hours

def get_wage():
    wage = float(input("Enter your hourly wage: ")) #Create a function that will input and return the hourly rate and is called inside the loop.
    return wage

def get_tax():
    tax = float(input("Enter income tax_rate: ")) #Create a function that will input and return the income tax rate and is called inside the loop.
    return tax

def gross_pay(hours, wage): # Gross pay
    gross = (wage * hours)
    return gross

def taxed(gross, tax): #Amount in Taxes
    amount_taxed = gross * tax
    return amount_taxed

def net_pay(gross, amount_taxed): # Net Pay
    net = gross - amount_taxed
    return net

def print_data(): # all data starts with 0. Then we enter data into emplist[] 6 items, get data for previous functions, and print that data
    tot_emp = 0
    tot_hours = 0.00
    tot_gross = 0.00
    tot_taxed = 0.00
    tot_net = 0.00

    EmpFile = open("Employees.txt", "r") # opening Employees.text in read only mode
    while True:
        runDate = input("Enter Start Date for report (MM/DD/YYYY) or 'All' for all data in file: ") # Here we are making an input on what to read
        if (runDate.upper() == "ALL"):
            break
        try:
            runDate = datetime.strptime(runDate, "%m/%d/%Y") #validating the rundate input
            break #remember that break. "breaks out" of the loop.
        except ValueError:
            print("Invalid Date Format. Try again.")
            print()
            continue #This will skip the next if statement, restart loop
        
    while True:
        EmpDetail = EmpFile.readline() #readline reads a line of the file and return it in the form of the string.
        if not EmpDetail: #once at the end of the file, if there is no data... break
            break
        EmpDetail = EmpDetail.replace("\n", "") #removes the carriage from the end of the line which would F%^k up our code
        empl_list = EmpDetail.split("|") # splits with the "|" acting as the seperator
        fromdate = empl_list[0]
       
        if (str(runDate).upper() != "ALL"): # Checking for the "ALL" input
            checkDate = datetime.strptime(fromdate, "%m/%d/%Y") # declares a variable named checkdate which holds the value of from date in a proper format
            if (checkDate < runDate): #if fromdate/checkdate is less than rundate, that is you're trying to look into the past until a certain point
                continue #then you won't print that line of data

        todate = empl_list[1]
        name = empl_list[2]
        hours = float(empl_list[3])
        wage = float(empl_list[4])
        tax = float(empl_list[5])
        gross = gross_pay(hours, wage)
        amount_taxed = taxed(gross, tax)
        net = net_pay(gross, amount_taxed)
        print(fromdate, todate, name, f'{hours:,.2f}', f'{wage:,.2f}', f'{gross:,.2f}', f'{tax:,.2f}', f'{amount_taxed:,.2f}', f'{net:,.2f}')
        tot_emp += 1
        tot_hours += hours
        tot_gross += gross
        tot_taxed += amount_taxed
        tot_net += net
        empl_totals["TotalEmp"] = tot_emp
        empl_totals["TotalHours"] = tot_hours
        empl_totals["TotalGross"] = tot_gross
        empl_totals["TotalTax"] = tot_taxed
        empl_totals["TotalNet"] = tot_net
        

def print_totals(empl_totals): # This prints out the data we input inside printdata()
    print()
    print(f'Total number of employees: {empl_totals["TotalEmp"]}')
    print(f'Total number of hours: {empl_totals["TotalHours"]:,.2f}')
    print(f'Total gross wage: {empl_totals["TotalGross"]:,.2f}')
    print(f'Total taxes deducted: {empl_totals["TotalTax"]:,.2f}')
    print(f'Total net pay: {empl_totals["TotalNet"]:,.2f}')




if __name__ == "__main__":

    EmpFile = open("Employees.txt", "a+") # opens our file. a is used to both read and append the file + creates if the file doesn't exist
    empl_totals = {}
    DetailsPrint = True
    while True:
    
        name = get_name()
        if (name.upper() == "END"):
            break
        fromdate, todate = get_dates()
        hours = get_hours()
        wage = get_wage()
        tax = get_tax()
        EmpDetail = fromdate + "|" + todate  + "|" + name  + "|" + str(hours) + "|" + str(wage)  + "|" + str(tax) + "\n"
        # Above here we are describing what will be written to our text files, the "|" exists to seperate data and the "\n" is used to make new lines in our txt file
        EmpFile.write(EmpDetail) # We are wrting to Employee.txt here from what we wrote in the Empdetail variable
    EmpFile.close() # Closing the employee.txt file
    
    print_data()
    if (DetailsPrint):#skips if no lines are printed
        print_totals(empl_totals)
    else:
        print("No detailed information to print")
        


    
