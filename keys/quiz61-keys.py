## Commit it in one script (.py)

your_email='hanz'
print("-----"+str(your_email)+"-------")

## Nomor 1
print('----1----')
input_1 = input('enter N :') 
input_1 = int(input_1)
## Process
input_1 = int(input_1/2)+1
output_1 = [(2*i)+1 for i in range(input_1)]
print('answer 1 :', output_1)

## Nomor 2
print('----2----')
input_2 = input('enter N :') 
input_2 = int(input_2)
## Process
output_2 = [1 + (1/n) for n in range(1,input_1) if 1 + (1/n) < 3*(1+(1/input_1))]
print('answer 2 :', output_2)

## Nomor 3

print('----3---')
input_3 = input('enter N :') 
input_3 = int(input_3)
## Process
print('answer 3 (below):')
for i in range(input_3) :
    list_word = [str(j+1) for j in range(i+1)]
    print('\n'+' '.join(list_word)+'\n')