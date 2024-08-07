# A simple expense tracker
This tracker takes the user's input and assigns a label to it (As an expenditure or a income). Then produces a list of the expenses (and also income) and puts it in a CSV file in your local machine. The data is structure using the The data is structured using the pandas. And the data can be displayed as a plot using matplotlib

## How to use this?
First check if you are on the latest version of python or not. Run this in your terminal

```
python --version
```
It should say Python 3.11.4

Next, Clone this GitHub respository:
```
git clone https://github.com/nrngxv/expense_tracker.git
```
You should get confirmation log saying the git repo has been cloned in your specified directory.

Next, run this command to start the program:
```
python3 main.py
```

## Explaination of the interface
You are presented with three options

1. Add a transaction
2. View transaction and summary within a date range
3. Exit Enter the option in the input field.

If a transaction is added, it asks for a date and the type of transactions it is (I for income and E for expense).
```
Enter the date of the transaction (dd-mm-YYYY format) or enter today's date:
Enter the category ('I' for income or 'E' for expense):
```

The date has to be in that specific format, or else it would return an error. Press enter to set to today's date dy default You also have the ability to add any description to the transaction that you have. This improves the quality of the input. This is the input field you will see for the description.
```
Enter a description(Optional):
```

View transaction would ask you to put a date range between which you would like to see the transaction, given that already have a list of transactions added.
You have to enter a start date from which you want to see the transaction list from
```
Enter the start date (dd-mm-YYYY):
```
Then you have put a end date. That is your range
```
Enter the end date (dd-mm-YYYY):
```

This will provide you with a transaction history which has clear labels. You also have the choice to Plot this whole data into Chart using MatPlotLib

```
Enter the start date (dd-mm-YYYY): 21-07-2024
Enter the end date (dd-mm-YYYY): 07-08-2024
Transactions form 21-07-2024 to 07-08-2024
      date  amount category               description
21-07-2024   100.0   Income Freelance project expense
21-07-2024   500.0  Expense                      Food
21-07-2024  1000.0  Expense                 More Food
06-08-2024   500.0   Income                   Project
07-08-2024   100.0   Income                      Food

Summary:
Total Income: 700.00 rupees
Total Expense: 1500.00 rupees
Net saving: -800.00 rupees
Do you want to see a plot? (y/n):
Input y to see the chart
```

And 3. Exit is self explanatory