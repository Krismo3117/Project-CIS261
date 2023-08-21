# Andrew Torres CIS261

import os

# Function to validate date format
def is_valid_date(date_str):
    try:
        from datetime import datetime
        datetime.strptime(date_str, '%m/%d/%Y')
        return True
    except ValueError:
        return False

# Function to calculate income tax
def calculate_income_tax(gross_pay, income_tax_rate):
    return gross_pay * (income_tax_rate / 100)

# Function to calculate net pay
def calculate_net_pay(gross_pay, income_tax):
    return gross_pay - income_tax

# Function to add employee record to the text file
def add_employee_record(file_name, from_date, to_date, employee_name, hours_worked, pay_rate, income_tax_rate):
    with open(file_name, 'a') as file:
        record = f"{from_date}|{to_date}|{employee_name}|{hours_worked}|{pay_rate}|{income_tax_rate}\n"
        file.write(record)

# Function to generate a report
def generate_report(file_name, target_date):
    total_employees = 0
    total_hours = 0
    total_tax = 0
    total_net_pay = 0

    with open(file_name, 'r') as file:
        for line in file:
            record = line.strip().split('|')
            from_date, to_date, employee_name, hours_worked, pay_rate, income_tax_rate = record

            if target_date == "All" or target_date == from_date:
                hours_worked = float(hours_worked)
                pay_rate = float(pay_rate)
                income_tax_rate = float(income_tax_rate)

                gross_pay = hours_worked * pay_rate
                income_tax = calculate_income_tax(gross_pay, income_tax_rate)
                net_pay = calculate_net_pay(gross_pay, income_tax)

                print(f"From Date: {from_date}")
                print(f"To Date: {to_date}")
                print(f"Employee Name: {employee_name}")
                print(f"Hours Worked: {hours_worked}")
                print(f"Hourly Rate: {pay_rate}")
                print(f"Gross Pay: {gross_pay}")
                print(f"Income Tax Rate: {income_tax_rate}%")
                print(f"Income Taxes: {income_tax}")
                print(f"Net Pay: {net_pay}")
                print()

                total_employees += 1
                total_hours += hours_worked
                total_tax += income_tax
                total_net_pay += net_pay

    print("Total Employees:", total_employees)
    print("Total Hours:", total_hours)
    print("Total Tax:", total_tax)
    print("Total Net Pay:", total_net_pay)

# Main program
if __name__ == "__main__":
    file_name = "employee_records.txt"

    while True:
        from_date = input("Enter From Date (mm/dd/yyyy) or 'All' to exit: ")
        
        if from_date.lower() == "all":
            break
        
        if not is_valid_date(from_date):
            print("Invalid date format. Please use mm/dd/yyyy format.")
            continue

        to_date = input("Enter To Date (mm/dd/yyyy): ")
        employee_name = input("Enter Employee Name: ")
        hours_worked = float(input("Enter Hours Worked: "))
        pay_rate = float(input("Enter Pay Rate: "))
        income_tax_rate = float(input("Enter Income Tax Rate (%): "))

        add_employee_record(file_name, from_date, to_date, employee_name, hours_worked, pay_rate, income_tax_rate)

    target_date = input("Enter the From Date for the report (mm/dd/yyyy) or 'All' for all records: ")
    generate_report(file_name, target_date)
