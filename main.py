#This files handles the main flow of the program

#importing different modules

import pandas as pd # this allows to load .csv file and work with it
import csv 
from datetime import datetime

#store data in a .csv file

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialise_csv(cls): #this is to load the CSV file, and structure it
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

CSV.initialise_csv()
CSV.add_entry("20-07-2024", 120, "Expense", "Medicines")





#TODO: view different transactions
#TODO: create a nice interface to view transactions

