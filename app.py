import csv
from datetime import datetime

FILE_NAME = "data.csv"


def Create_file():
    try:
        file = open(FILE_NAME, mode="x", newline="")
        writer = csv.writer(file)
        writer.writerow(["Date", "Expence", "Amount", "Notes"])
    except FileExistsError:
        pass


def add_exp():
    CurrentTime = datetime.now().strftime("%d-%m-%y")
    expense = str(input("Enter Food,Travel,Shopping--->"))
    Amount = int(input("Enter Your Amount:-->"))
    Notes = str(input("Enter Your Notes-->"))
    NewFile = open(FILE_NAME, mode="a", newline="")
    writer = csv.writer(NewFile)
    writer.writerow([CurrentTime, expense, Amount, Notes])

    print("Add Expence Succesfullly")


def show_exp():
    showexp = open(FILE_NAME, mode="r")
    writer = csv.reader(showexp)
    next(showexp)
    for row in showexp:
        print("Your Expecnce show==>", row)


def summary_exp():
    summary = {}
    total_amount = 0
    summaryexp = open(FILE_NAME, mode="r")
    reader = csv.reader(summaryexp)
    next(reader)
    # print(summaryexp)
    for row in reader:
        expence_cata = row[1]
        expence_amount = int(row[2])

        if expence_cata in summary:
            summary[expence_cata] += expence_amount
        else:
            summary[expence_cata] = expence_amount

    
        total_amount = expence_amount + total_amount
    print(summary)
    print("Your Total Bill:-->",total_amount)



while True:
    Create_file()
    print("======Event Expence Management======")
    print("1:=>Add Expence")
    print("2:=>Show Expence")
    print("3:=>Summary")
    print("4:=>Exit")

    choice = int(input("Enter Your Choice:-->"))

    if choice == 1:
        # print("Add Expence")
        add_exp()
    elif choice == 2:
        # print("Show Expence")
        show_exp()
    elif choice == 3:
        # print("Summary Expence")
        summary_exp()
    elif choice == 4:
        print("Thanks For Visiting")
        break
