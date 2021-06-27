#######################
## Complete The Codes##
#######################

your_email=...
print("-----"+str(your_email)+"-------")

## input the function,

def weighted_avg(X,w):
    '''input X : X adalah list dengan panjang N'''
    '''input w : w adalah list dengan panjang N'''
    
    '''output w_avg : one float value'''
    '''Formula : (x1*w1 + x2*w2 + x3*w3 + ... + xN*wN)/(w1+w2+w3+...+wN)'''
    sum_all = 0
    w_all = 0
    for i,j in zip(X,w):
        sum_all += i*j
        w_all += j
    w_avg = sum_all/w_all
    
    return w_avg

def emp_score(X):
    '''input X : X is list'''
    '''output eSco : one float value'''
    '''Formula : ((first value of X + last value of X)/2)+(3.5+second value of X)+(Avg of Y dimana Y adalah list baru yang dimana semua nilai X di pangkat 0.5)'''
    
    v1 = (X[0]+X[-1])/2
    v2 = 2.5 + X[1]
    v3 = sum([i**0.5 for i in X])/len(X)# --> lengkapi
    
    eSco = v1+v2+v3
    
    return eSco

def combine_value(X):
    '''input X : X is dictionary'''
    
    '''A = list of Weighted Average Siswa'''
    '''B = list of Scoring Employee'''
    
    c_val = (X['len_A']+X['len_B'])/2
    
    return c_val

## The Data ..
PATH_DIR = '../python_begin/files/'
Open_A = open(PATH_DIR + 'nilai_siswa.txt') # --> nilai_siswa.txt
read_A = Open_A.readlines() # --> readlines
List_A_float = [] # --> change data to float
for i in read_A:
    all_numb = i.split(',')
    List_A_float.append([float(j) for j in all_numb])

## weight
Open_W = open(PATH_DIR + 'nilai_siswa_weight.txt') # --> nilai_siswa_weight.txt
read_W = Open_W.readlines() # --> readlines
List_W_float = [] # --> change data to float
for i in read_W:
    all_numb = i.split(',')
    List_W_float.append([float(j) for j in all_numb])


Open_B = open(PATH_DIR + 'employee_factor.txt') # --> employee_factor.txt
read_B = Open_B.readlines() # --> readlines
List_B_float = [] # --> change data to float
for i in read_B:
    all_numb = i.split(',')
    List_B_float.append([float(j) for j in all_numb])



## Process
all_was = [weighted_avg(i,j) for i,j in zip(List_A_float, List_W_float)]
Avg_was = sum(all_was)/len(all_was)

all_scoring = [emp_score(i) for i in List_B_float]
Avg_asc = sum(all_scoring)/len(all_scoring)

Max_was = max(all_was)

Min_asc = min(all_scoring)

input_comb = {'len_A': len(all_was),'len_B': len(all_scoring)}
cval = combine_value(input_comb)


## output (2 digits after comma)
print('Avg Weighted Average Siswa : %.2f' % Avg_was)
print('Avg Scoring Employee : %.2f' % Avg_asc)
print('Max Value Weighted Average Siswa : %.2f' % Max_was)
print('Min Value Scoring Employee : %.2f' % Min_asc)
print('Combine Value : %.2f' % cval)

print('-----------------------------------------')