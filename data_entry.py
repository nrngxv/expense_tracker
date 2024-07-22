from datetime import datetime

#VARs
date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E":"Expense"}

#getting the date input
def get_date(prompt, allow_default=False): #set allow_default to True to auto set default value
    date_str = input(prompt) #pass value from user input to a variable

    if allow_default and not date_str: #this allows for reverting back to default is user input is not present
        #strftime converts date into string format (date-month-year)
        return datetime.today().strftime(date_format) 
    
    try:
        #converting the input into the datetime format dd-mm-YYYY
        valid_date = datetime.strptime(date_str, date_format) #strptime converts date str into datetime object
        
        #returing the datetime as a string 
        return valid_date.strftime(date_format) 
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

#getting the amount input
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <=0: #validates the input for being right, if not then raise ValueError
            raise ValueError("Amount must be a non-negetive non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

#getting the category input
def get_category():
    category = input("Enter the category ('I' for income or 'E' for expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category] #this is calling the value from the dictionary CATEGORIES
    else:
        print("Invalid category. Please enter 'I' for income or 'E' for expense")
        return get_category()

#getting the description input
def get_description():
    return input("Enter a description (Optional): ")