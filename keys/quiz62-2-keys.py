
FILE_DIR = '../python_begin/files/quiz_6.txt'
file1 = open(FILE_DIR,"r") 
A = file1.readlines()[0]
A = A.split(',')
A = [int(i) for i in A]

N = int(input('N :'))

now = A[0]
count_turun = 0
for i in range(1,len(A)-1):
    diff = A[i] - now
    if diff < 0:
        count_turun += 1
        
    if count_turun == N:
        break
    else:
        now = A[i]
        
print('di hari ke-',i)
    