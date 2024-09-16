# TOPIC - RECURSION


fac = 1
# for i in range(1, 5+1):
#     fac *= i
#     print(fac)
i = 5
# while 0<+i:
#     fac *= i
#     i-=1
# print(fac)

def factorial (par):
    if (par == 0 or par == 1):
        return 1
    else:
        return par * factorial(par-1)
    
    
# print(factorial(5))


# def sum(num):
#   if num == 0 or num == 1:
#     return 1
  
#   else:
#     return num + sum(num-1)
# ans = sum(5);

# print(ans)



li = [1,2,6,88,4545,12]

for i in range(li[i]):
    print(li[i])

    
    
list = [1,2,6,88,4545,12]


def printli(para, indx = 0):
    if indx == len(para):
        return
    print(list[indx])
    printli(para, indx +1)
        
        
printli(list)
    
    
    
    
    
    
