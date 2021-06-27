#######################
## Complete The Codes##
#######################

your_email=...
print("-----"+str(your_email)+"-------")

## Input the data
price = input('put the price : ')
items = input('put the number of items : ')
percentage = input('pct in decimal : ')

price = float(price)
items = int(items)
percentage = float(percentage)

## check if price between 10000 and 25000 or not, percentage between 25 and 45, items > 0, then Process
if (price>=10000) & (price<=25000) & (percentage>=0.25) & (percentage<=0.45):
## Process
## Rule : (Basic Price + (price times items)) substract with the discount (%), basic price = 25000

    total_price = (25000+(price*items))*(1-percentage)
    
    ## output (2 digits after comma)
    print('Total Price : %.2f' % total_price)
    
elif price<10000:
    print('ERROR 1')
elif price>25000:
    print('ERROR 2')
elif percentage<0.25:
    print('ERROR 3')
elif percentage>0.45:
    print('ERROR 4')
elif items<=0:
    print('ERROR 5')
## print error. The Error message is depend on the mistake
## if price less than 10000 --> ERROR 1.
## if price more than 25000 --> ERROR 2.
## if percentage less than 25 --> ERROR 3.
## if percentage more than 45 --> ERROR 4.
## if items <= 0 --> ERROR 5.
else:
    print('Others')

## scoring
print('-----------------------------------------')

## Hint : "if" can be more than 1 times