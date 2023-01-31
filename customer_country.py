import csv

read = open('customers.csv', 'r')
customer_outfile = open('customer_country.csv', 'w')

customer_infile = csv.reader(read, delimiter=',')

next(customer_infile)
for record in customer_infile:
    # print(record)
    customer_outfile.write(
        record[1] + ',' + record[2] + ',' + record[4] + '\n')

read.close()
customer_outfile.close()
