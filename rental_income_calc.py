# Rental Income Calculator
# The purpose of this program is to calculate the Return on Investment(ROI) of a given property
# There can be multiple users
# Users can add multiple incomes and expenses
# Users can add mortgage, mortgage interest rate and terms of their mortgage



class UserIncomes():

    """

    this class holds information about the 
    different types of income the property
    generates

    class UserIncomes will have the following attributes:
        income_name
        income_amount

    Attribute types:
        income_name = string
        income_amount = float

    """

    def __init__(self, income_name, income_amount):
        self.income_name = income_name
        self.income_amount = income_amount



class UserExpenses():
    """

    this class holds information about the 
    different types of expenses the property
    will occur

    class UserExpenses will have the following attributes:
        expense_name
        expense_amount

    Attribute types:
        expense_name = string
        expense_amount = float

    """
    def __init__(self, expense_name, expense_amount):
        self.expense_name = expense_name
        self.expense_amount = expense_amount



class UserProperty():
    """
    
    class UserProperty will have the following attributes:
        name
        purchase_cost

    Attribute types:
    name = string
    purchase_cost = float
    mortgage = float
    mortgage_interest = float
    mortgage_loan_term = integer
    self.income_type = []
    self.expense_type =[]
    
    """

    def __init__(self, name, purchase_cost):
  
        self.name = name
        self.purchase_cost = purchase_cost
        self.mortgage = 0 # setting default to 0 as this will be changed by user
        self.mortgage_interest = 0 # setting default to 0 as this will be changed by user
        self.mortgage_loan_term = 0 # setting default to 0 as this will be changed by user
        self.income_type = [] # there will be various incomes that the user will have
        self.expense_type = [] # there will be various expenses that the user will have

    # setting the information needed for mortgage
    def mortgage_parameters(self, mortgage_amount, interest, loan_term):

        self.mortgage = mortgage_amount
        self.mortgage_interest = interest
        self.mortgage_loan_term = loan_term

    def input_income(self, income_name, income_amount):

        prop_income = UserIncomes(income_name, income_amount)
        self.income_type.append(prop_income)

    def input_expense(self, expense_name, expense_amount):

        prop_expense = UserExpenses(expense_name, expense_amount)
        self.expense_type.append(prop_expense)

    def cash_flow(self):

        monthly_interest = self.mortgage_interest / 12 / 100
        total_payments = self.mortgage_loan_term * 12

        # default formula to calculate mortgage based on this: M = P [ I(1 + I)^N ] / [ (1 + I)^N − 1]
        # source: https://www.rocketmortgage.com/learn/how-to-calculate-mortgage
        total_mortgage_pmt = (self.mortgage * monthly_interest) / (1 - (1 + monthly_interest) ** total_payments) 

        # calculate incomes
        income_total = 0
        for income in self.income_type:
            income_total += income.income_amount

        # calculate expenses
        expense_total = 0
        for expense in self.expense_type:
            expense_total += expense.expense_amount
            expense_total += total_mortgage_pmt

        # net income
        net_income = income_total - expense_total
        
        return net_income


    def roi_calculation(self):

        income_total = 0
        for income in self.income_type:
            income_total += income.income_amount

        # calculate expenses
        expense_total = 0
        for expense in self.expense_type:
            expense_total += expense.expense_amount

        # net income
        net_income = income_total - expense_total

        #roi
        roi = (net_income / self.purchase_cost) * 100
        
        return roi


    def cash_on_cash_roi(self):

        yearly_cash_flow = self.cash_flow() * 12
        investment = self.purchase_cost
        cash_on_cash_roi = (yearly_cash_flow / investment) * 100
        return cash_on_cash_roi
    
class User:

    """

    this class holds information about the
    user

    class User will have the following attributes:
        username
        user property

    Attribute types:
        username = string
        user_property = [] in case they have more than 1 property to add

    """
    def __init__(self, username):

        self.username = username
        self.user_property = []

    def log_property(self, add_property):

        self.user_property.append(add_property)

def run():

        # this is what the user will interact with
    print("\n-------------- | Welcome to the Rental Income Calculator |-------------")

    users = {}

    while True:

        print("\n")
        print("\n|".center(10) + " (N)EW USER ".center(23) + "|".center(25))
        print("\n|".center(10) + " (U)SER LOGIN ".center(25) + "|".center(21))
        print("\n|".center(10) + " (E)XIT PROGRAM ".center(27) + "|".center(17))
        print("\n")
        print("".center(70, "-"))
    

        response = input("\nPlease make a selection: 'n', 'u' or 'e'. ").lower().strip()


        if response == "n":

            username = input("\nPlease enter a username: ").lower()
            users[username] = User(username)

            print(f"\n{username} created successfully")

        elif response == "u":

            username = input("\nEnter your username to continue: ")

            if username.lower() in users:
                user = users[username]

                while True:

                    print("\nWhat would you like to do?: Select 'a', 'c' or 'l':  ")
                    print("\n|".center(10) + " (A)DD A PROPERTY ".center(23) + "|".center(25))
                    print("\n|".center(10) + " (C)ALCULATE ROI ".center(25) + "|".center(22))
                    print("\n|".center(10) + " (L)OG OUT ".center(23) + "|".center(25))
                    login_response = input("\nSelect 'a', 'c' or 'l': ").lower().strip()

                    print("".center(70, "-"))

                    if login_response == "a":

                        print("\nADD PROPERTY")
                        print("".center(70, "-"))

                        property_name = input("\nEnter the name of your property: ")
                        purchase_cost = float(input("\nEnter the purchase cost of your property: "))
                        add_property = UserProperty(property_name, purchase_cost)

                        print(f"\n{property_name} has been successfuly added.")
                        print("".center(70, "-"))

                        # input mortgage info
                        print("\nADD MORTGAGE INFORMATION")
                        print("".center(70, "-"))

                        mortgage = float(input("\nWhat is the mortgage cost per month?: "))
                        mortgage_interest = float(input("\nWhat is the mortgage interest cost per month(in dollars?): "))
                        mortgage_loan_term = int(input("\nWhat is the loan term (in years) of the mortgage?: "))
                        add_property.mortgage_parameters(mortgage, mortgage_interest, mortgage_loan_term)

                        print("\nMortgage information successfully added.")
                        print("".center(70, "-"))

                        # input income
                        print("\nADD INCOMES EARNED FROM PROPERTY")
                        print("".center(70, "-"))

                        total_incomes = int(input("\nHow many types of income would you like to enter?: "))

                        for _ in range (total_incomes): # this will do a loop for user to enter the incomes they have
                            income_source = input("\nEnter the source of income: ")
                            income_amount = float(input(f"How much does {income_source.upper()} generate per month?: "))
                            add_property.input_income(income_source, income_amount)

                            print(f"\n{income_source.upper()} has been successfully added.")
                            print("".center(70, "-"))

                        # input expense
                        print("\nADD PROPERTY EXPENSES")
                        print("".center(70, "-"))

                        total_expenses = int(input("\nHow many types of expenses would you like to enter?: "))

                        for _ in range (total_expenses): # this will do a loop for user to enter the incomes they have
                            expense_source = input("\nEnter the type of expense: ")
                            expense_amount = float(input(f"How much does {expense_source.upper()} cost per month?: "))
                            add_property.input_expense(expense_source, expense_amount)

                            print(f"\n{expense_source.upper()} has been successfully added.")

                            
                        # add user information to list
                        print("".center(70, "-"))
                        print("\nAll information has been added successfully")
                        print(f"{property_name} has been updated.")
                        user.log_property(add_property)
                        print("".center(70, "-"))

                        # display list of properties
                    elif login_response == 'c':

                        if not user.user_property:
                            print("\nThere are no properties listed. ")

                            continue


                        print("\nPROPERTY LIST")
                        print("".center(70, "-"))

                        for index, add_property in enumerate(user.user_property, start=1):
                            print(f"\n{index}: {add_property.name.upper()}")

                        property_number = int(input("\nSelect a property by number: ")) - 1
                        property_selection = user.user_property[property_number]

                        property_cash_flow = property_selection.cash_flow()
                        property_roi = property_selection.roi_calculation()
                        coc_roi = property_selection.cash_on_cash_roi()

                        print("\n-------------- | POTENTIAL RETURN ON INVESTMENT |-------------")
                        print("\n\tNote: the figures below are an estimate.")

                        print(f"\nProperty Name: {property_selection.name.upper()}".center(50))
                        print(f"\nAnnual Cash Flow: ${property_cash_flow:.2f}".center(50))
                        print(f"Approximate ROI: {property_roi:.2f}%")
                        print(f"Cash-On-Cash ROI: {coc_roi:.2f}%")

                    # if there isn't a user found
                    elif login_response == 'l':
                        print("\nReturning to main menu.")

                        break
                    else:
                        print("Invalid entry. Please try again.")
            else:
                print("Sorry. User is not found. Please try again.")

        elif response == 'e':

            print("\nThank you for using the program!")

            break
        else:
            print("Invalid entry. Please try again.")

                            
if __name__ == "__main__":

    run()


            



 
        


    


