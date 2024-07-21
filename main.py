#This files handles the main flow of the program

#importing different modules
import pandas as pd # this allows to load .csv file and work with it
import csv 
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

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
        df = pd.read_csv(cls.CSV_file) #reading from the CSV file throught the method
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT) #accessing rows for date, converting them into objects

        #it converts the str value to a obj which makes it easier to filter through dates
        start_date = datetime.strptime(start_date, CSV.FORMAT) #converting startdate from str to obj
        end_date = datetime.strptime(end_date,CSV.FORMAT) #same here too, str to obj

        #
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        #location where the var mask is true
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transaction forund in the given date range")
        else:
            print(f"Transactions form {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            #This sorts through the filtered_df, where the category is income and takes the amount and sums them
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            print("\nSummary: ")
            print(f"Total Income: {total_income:.2f} rupees")
            print(f"Total Expense: {total_expense:.2f} rupees")
            print(f"Net saving")



def add():
    CSV.initialise_csv()
    date = get_date("Enter the date of the transaction (dd-mm-YYYY format) or enter today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


# ***main flow***

add()


#TODO: view different transactions
#TODO: create a nice interface to view transactions