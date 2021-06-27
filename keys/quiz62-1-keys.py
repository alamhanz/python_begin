
FILE_DIR = '../python_begin/files/quiz_6.txt'
file1 = open(FILE_DIR,"r") 
A = file1.readlines()[0]
A = A.split(',')

print(type(A))

x = input('x :')
y = input('y :')
output = []
kx = ky = 0
for i in A:
    if kx > ky:
        break
    if x == i:
        kx += 1
        output.append(i)
    elif y == i:
        ky += 1
        output.append(i)
print(output)