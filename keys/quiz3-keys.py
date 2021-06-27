#######################
##       Codes       ##
#######################

# your_email=...
# print("-----"+str(your_email)+"-------")

## 
A=[16, 17,  9, 20, 20, 12,  5, 12, 16, 10, 17, 15,  1, 16,  4,  6,  6,
        4,  0,  2, 12, 15,  6,  4, 16, 12, 16, 20,  1, 16, 16, 20,  2,  6,
        2, 10, 16, 17,  6,  4,  6,  6,  8, 10,  5,  1,  2, 15,  2,  8,  8]
B=[20, 36, 29, 24, 24, 30, 31, 37, 30, 31, 32, 34, 39, 34, 20, 28, 20,
       23, 36, 40, 20, 29, 37, 29, 35, 33, 40, 23, 23, 37, 20, 33, 30, 24,
       32, 23, 32, 40, 30]
C=[12, 10, 15, 26, 24, 18, 23, 18, 23, 28, 11, 18, 18, 23, 28, 10, 12,
       10, 18, 11, 25, 18, 24, 23, 11, 12, 18, 25, 28, 17, 20, 28, 15, 20,
       24, 18, 29, 23, 21, 29, 25, 26, 26, 16, 23, 23, 25, 11, 23]


## Ubah list A, B, C diatas menjadi seperti :
# A1=list semua angka unik >0 tapi <=15 dari A, B dan C
# B1=list semua angka unik >15 tapi <=30 dari A, B dan C

base_number1 = list(range(1,16))
base_number2 = list(range(16,31))
A1 = list(set(A+B+C) & set(base_number1))
B1 = list(set(A+B+C) & set(base_number2))

print('A1 =',A1)
print('B1 =',B1)

# Clue : Set bisa jadi List, atau sebaliknya