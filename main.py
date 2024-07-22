#This files handles the main flow of the program

#importing different modules
import pandas as pd # this allows to load .csv file and work with it
import csv 
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt


#store data in a .csv file
class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    #this is to load the CSV file, and structure it
    def initialise_csv(cls):

        try:
            pd.read_csv(cls.CSV_FILE) #Loading in CSV_FILE variable 
        except FileNotFoundError: #if the file does not exists
            df = pd.DataFrame(COLUMNS = ["date","amount","category","description"]) #dataframe creates columns with the file
            df.to_csv(cls.CSV_FILE, index=False) #the dataframe is converted to csv

    @classmethod
    def add_entry(cls, date, amount, category, description):
        #using dictionaries so the data is in the correct writers 
        new_entry = { 
            "date": date,
            "amount": amount,
            "category": category,
            "description": description 
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = cls.COLUMNS)
            writer.writerow(new_entry)
        print("Enter added successfully")

    @classmethod
    #accessing the list of transactions.
    def get_transaction(cls, start_date, end_date):

        #reading from the CSV file throught the method
        df = pd.read_csv(cls.CSV_FILE)
        #accessing rows for date, converting them into objects
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)

        #it converts the str value to a obj which makes it easier to filter through dates
        start_date = datetime.strptime(start_date, CSV.FORMAT) #converting startdate from str to obj
        end_date = datetime.strptime(end_date,CSV.FORMAT) #same here too, str to obj
        
        #this mask is used to filter all the data in the dataframe
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        #applying the mask. it gives location where the var mask is true
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transaction forund in the given date range")
        else:
            #this is a transaction summary
            print(f"Transactions form {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            #This sorts through the filtered_df, where the category is income and takes the amount and sums them
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            #printing data
            print("\nSummary: ")
            print(f"Total Income: {total_income:.2f} rupees") #.2f prints decimal upto the second value
            print(f"Total Expense: {total_expense:.2f} rupees")
            print(f"Net saving: {(total_income - total_expense):.2f} rupees")

#making a graph plot using matplotlib
def plot_transactions(df):
    df.set_index("date", inplace=True) #inplace set:True to return "None"

    #this creates income_df with "category rows" with only income
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)

    #this creates income_df with "category rows" with only expense
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5)) #setting the size of the graph

    plt.plot(income_df.index, income_df["amount"], label="Income", colour="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", colour="g")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses over time")
    plt.legend()
    plt.grid(True)
    plt.show()


#adding transactions
def add():
    CSV.initialise_csv()
    date = get_date("Enter the date of the transaction (dd-mm-YYYY format) or enter today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


#main flow
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary with in a date range")
        print("3. Exit")
        user_input = input("Enter your option (1-3): ")
        
        if user_input == "1":
            add()
        elif user_input == "2":
            #as we already have a function for fetching date, we use it
            start_date = get_date("Enter the start date (dd-mm-YYYY): ")
            end_date = get_date("Enter the end date (dd-mm-YYYY): ")

            #now we just need to pass the data to our file
            df = CSV.get_transaction(start_date, end_date) #putting df for plotting in a graph  
            if input("Do you want to see a plot? (y/n): ").lower() == "y":
                plot_transactions(df)

        elif user_input == "3":
            print("Shutting program down")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

#prevents from directly running the file
if __name__ == "__main__":
    main()