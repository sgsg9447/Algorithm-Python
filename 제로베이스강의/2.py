def factorial(num):
    if num>1:
        return num * factorial(num-1)
    else:
        return num

for num in range(10):
    print(factorial(num)) 


def factorial2(num):
    if num<=1:
        return num
    return_val = num * factorial2(num-1)
    return(return_val)

def factorial3(num):
    if num<=1:
        return num
    return(num * factorial3(num-1))

for num in range(10):
    print(factorial(num)) 


for num in range(10):
    print(factorial2(num)) 


for num in range(10):
    print(factorial3(num)) 
