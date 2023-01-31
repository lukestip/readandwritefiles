# employee_bonus.py - program that reads the EmployeePay.csv file
# and prints out details of each employee
import csv

epRead = open('EmployeePay.csv', 'r')

employee_infile = csv.reader(epRead, delimiter=',')


next(employee_infile)
for record in employee_infile:
    print('ID: '+record[0])
    print('First Name: '+record[1])
    print('Last Name: '+record[2])
    print('Pay: '+record[3])
    print('Bonus: '+record[4])

epRead.close()
