#######################
## Complete The Codes##
#######################

your_email='alamhanz'
print("-----"+str(your_email)+"-------")

## Input the data
price = input('put the price : ')
items = input('put the number of items : ')
percentage = input('Discount in Decimal : ')

price = float(price)
items = float(items)
percentage = float(percentage)

## Process
## Rule : (Basic Price + (price times items)) substract with the discount (%), basic price = 25000

total_price = 25000 + (price*items)
total_price = total_price*(1-percentage)

## output (2 digits after comma)
print('Total Price :',total_price)


## scoring
print('-----------------------------------------')