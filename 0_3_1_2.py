# https://ctflearn.com/challenge/174 

# Can you help me? 
# I need to know how many lines there are where the number of 
# 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. 
# Please! Here is the file: 
# https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys

lines = []
with open('data.dat') as f:
    lines = f.readlines()

zero_count = 0
one_count=0
flag_count = 0
for line in lines:
    zero_count = 0
    one_count = 0
    for char in line:
        if char == '0':
            zero_count+=1
        if char == '1':
            one_count +=1
    if zero_count % 3 == 0 or one_count % 2 == 0:
        flag_count += 1
    print(f'Zero: {zero_count} One: {one_count}')
print(f'FLAG: {flag_count}')
    
            
