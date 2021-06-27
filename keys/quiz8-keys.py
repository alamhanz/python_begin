#######################
## Complete The Codes##
#######################

import numpy as np
import matplotlib.pyplot as plt

your_email='alam'
print("-----"+str(your_email)+"-------")

## The Data ..
PATH_DIR = '../python_begin/files/'
PATH_IMG = '../python_begin/images/'
orders_customers = open(PATH_DIR + 'daily_trx.txt') # --> daily transaction
orders_customers = orders_customers.readlines() # --> readlines
orders_customers = [i.split(',') for i in orders_customers]

daily_orders = [len(x) for x in orders_customers]

cust_ind_orders = {}
for ord in orders_customers:
    for cc in ord :
        if cc not in cust_ind_orders.keys():
            cust_ind_orders[cc] = 1
        else:
            cust_ind_orders[cc] += 1
            
cust_list = cust_ind_orders.keys()
total_order_list = cust_ind_orders.values()

## First Plot 
x1 = np.arange(len(daily_orders))
plt.figure(figsize=(15,8))
plt.plot(x1, daily_orders)
plt.xlabel('day')
plt.ylabel('number of daily orders')
plt.title('Daily Order Plot')
plt.legend(['orders'])
plt.savefig(PATH_IMG+'Daily_orders.png')
plt.clf()

## Second Plot
plt.figure(figsize=(15,8))
plt.plot(cust_list, total_order_list)
plt.xlabel('customer ids')
plt.ylabel('number of orders')
# plt.xticks(rotation=90)
plt.title('Total Order Customers')
plt.savefig(PATH_IMG+'Customer_orders.png')
