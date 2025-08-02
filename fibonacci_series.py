# Writing a FIBONACCI SERIES
fib=[0,1]
#Range starts from 0 by default
n=5
for i in range(n):
    fib.append(fib[-1]+fib[-2])
    
#converting the list of integers to a string
print(', '.join(str(e) for e in fib))