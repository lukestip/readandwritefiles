# customer_sales_report.py - program that reads the sales.csv file
# and creates a new file with the customer ID and calculated total
import csv

# Open files
read = open('sales.csv', 'r')
infile_salesCSV = csv.reader(read, delimiter=',')

# create list to consolidate order ID totals
salesList = [0.0]
count = 0
idNum = 250

next(infile_salesCSV)
for row in infile_salesCSV:
    if idNum == int(row[0]):
        salesList[count] += round(float(row[3]) +
                                  float(row[4])+float(row[5]), 2)
    else:
        salesList.append(0.0)
        idNum += 1
        count += 1
        salesList[count] += round(float(row[3]) +
                                  float(row[4])+float(row[5]), 2)


read.close()

# Open outfile
outfile_salesreport = open('salesreport.csv', 'w')

outfile_salesreport.write("Customer,Total\n")

idNum = 250
for i in salesList:
    outfile_salesreport.write(str(idNum)+','+str(i)+'\n')
    idNum += 1

outfile_salesreport.close()
