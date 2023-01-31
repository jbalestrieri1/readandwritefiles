with open('sales.csv', 'r') as in_file:
    header = in_file.readline()
    calc = {}
    for line in in_file:
        data = line.strip().split(',')
        customer_id = data[0]
        calculation = float(data[3])

        if customer_id in calc:
            calc[customer_id]['total_sales'] = + calculation
        else:
            calc[customer_id] = {
                'num_orders': 1,
                'total_sales': calculation
            }

with open('sales_report.csv', 'w') as out_file:
    out_file.write('CustomerID TotalSales\n')
    for customer_id, data in calc.items():
        out_file.write(f"{customer_id}{data['total_sales']:2f}\n")
