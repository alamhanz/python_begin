PATH_DIR = '../python_begin/files/'

file1 = open(PATH_DIR+'A.txt',"r") 
A_txt = file1.readlines()[0]

file1 = open(PATH_DIR+'B.txt',"r") 
B_txt = file1.readlines()[0]

file1 = open(PATH_DIR+'C.txt',"r") 
C_txt = file1.readlines()[0]


A_txt_list = A_txt.split(',')
B_txt_list = B_txt.split(',')
C_txt_list = C_txt.split(',')
All_txt = A_txt_list+B_txt_list+C_txt_list

print('1.')
print(A_txt_list.index('forgotten'))

print('\n2.')
print(B_txt_list.index('imperception'))

print('\n3.')
print(len(set(All_txt)))
